# -*- coding: utf-8 -*-

# Copyright 2022-2023 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://bunkrr.su/"""

from .lolisafe import LolisafeAlbumExtractor
from .. import text
from urllib.parse import urlsplit, urlunsplit

MEDIA_DOMAIN_OVERRIDES = {
    "cdn9.bunkr.ru" : "c9.bunkr.ru",
    "cdn12.bunkr.ru": "media-files12.bunkr.la",
    "cdn-pizza.bunkr.ru": "pizza.bunkr.ru",
}

CDN_HOSTED_EXTENSIONS = (
    ".mp4", ".m4v", ".mov", ".webm", ".mkv", ".ts", ".wmv",
    ".zip", ".rar", ".7z",
)


class BunkrAlbumExtractor(LolisafeAlbumExtractor):
    """Extractor for bunkrr.su albums"""
    category = "bunkr"
    root = "https://bunkrr.su"
    pattern = r"(?:https?://)?(?:app\.)?bunkr+\.(?:la|[sr]u|is|to)/a/([^/?#]+)"
    example = "https://bunkrr.su/a/ID"

    def fetch_album(self, album_id):
        # album metadata
        page = self.request(self.root + "/a/" + self.album_id).text
        info = text.split_html(text.extr(
            page, "<h1", "</div>").partition(">")[2])
        count, _, size = info[1].split(None, 2)

        pos = page.index('class="grid-images')
        urls = list(text.extract_iter(page, '<a href="', '"', pos))

        return self._extract_files(urls), {
            "album_id"   : self.album_id,
            "album_name" : text.unescape(info[0]),
            "album_size" : size[1:-1],
            "description": text.unescape(info[2]) if len(info) > 2 else "",
            "count"      : len(urls),
        }

    def _extract_files(self, urls):
        for url in urls:
            if url.startswith("/"):
                try:
                    page = self.request(self.root + text.unescape(url)).text
                    if url[1] == "v":
                        url = text.extr(page, '<source src="', '"')
                    else:
                        url = text.extr(page, '<img src="', '"')
                except Exception as exc:
                    self.log.error("%s: %s", exc.__class__.__name__, exc)
                    continue

            else:
                if url.lower().endswith(CDN_HOSTED_EXTENSIONS):
                    scheme, domain, path, query, fragment = urlsplit(url)
                    if domain in MEDIA_DOMAIN_OVERRIDES:
                        domain = MEDIA_DOMAIN_OVERRIDES[domain]
                    else:
                        domain = domain.replace("cdn", "media-files", 1)
                    url = urlunsplit((scheme, domain, path, query, fragment))

            yield {"file": text.unescape(url)}
