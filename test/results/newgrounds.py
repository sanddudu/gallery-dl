# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import newgrounds


__tests__ = (
{
    "#url"     : "https://www.newgrounds.com/art/view/tomfulp/ryu-is-hawt",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#urls"        : "https://art.ngfiles.com/images/1993000/1993615_4474_tomfulp_ryu-is-hawt.44f81090378ae9c257a5e46a8e17cc4d.gif?f1695674895",
    "#sha1_content": "8f395e08333eb2457ba8d8b715238f8910221365",

    "artist"     : ["tomfulp"],
    "comment"    : "Consider this the bottom threshold for scouted artists.In fact consider it BELOW the bottom threshold.",
    "date"       : "dt:2009-06-04 14:44:05",
    "description": "Consider this the bottom threshold for scouted artists.  In fact consider it BELOW the bottom threshold.   ",
    "favorites"  : int,
    "filename"   : "1993615_4474_tomfulp_ryu-is-hawt.44f81090378ae9c257a5e46a8e17cc4d",
    "height"     : 476,
    "index"      : 1993615,
    "rating"     : "e",
    "score"      : float,
    "tags"       : [
        "ryu",
        "streetfighter",
    ],
    "title"      : "Ryu is Hawt",
    "type"       : "article",
    "user"       : "tomfulp",
    "width"      : 447,
},

{
    "#url"     : "https://art.ngfiles.com/images/0/94_tomfulp_ryu-is-hawt.gif",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#urls"    : "https://art.ngfiles.com/images/1993000/1993615_4474_tomfulp_ryu-is-hawt.44f81090378ae9c257a5e46a8e17cc4d.gif?f1695674895",
},

{
    "#url"     : "https://www.newgrounds.com/art/view/sailoryon/yon-dream-buster",
    "#comment" : "embedded file in 'comments' (#1033)",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#urls"    : (
        "https://art.ngfiles.com/images/1438000/1438673_sailoryon_yon-dream-buster.jpg?f1601058173",
        "https://art.ngfiles.com/comments/172000/iu_172374_7112211.jpg",
    ),
},

{
    "#url"     : "https://www.newgrounds.com/art/view/zedrinbot/lewd-animation-tutorial",
    "#comment" : "extra files in 'art-image-row' elements - WebP to GIF (#4642)",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#urls"    : (
        "https://art.ngfiles.com/images/5091000/5091275_45067_zedrinbot_untitled-5091275.0a9d27ed2bc265a7e89478ed6ad6f86f.gif?f1696187399",
        "https://art.ngfiles.com/images/5091000/5091275_45071_zedrinbot_untitled-5091275.6fdc62eaef43528fb1c9bda624d30a3d.gif?f1696187437",
        "https://art.ngfiles.com/images/5091000/5091275_45070_zedrinbot_untitled-5091275.0d7334746374465bd448908b88d1f810.gif?f1696187435",
        "https://art.ngfiles.com/images/5091000/5091275_45072_zedrinbot_untitled-5091275.6fdc62eaef43528fb1c9bda624d30a3d.gif?f1696187438",
        "https://art.ngfiles.com/images/5091000/5091275_45073_zedrinbot_untitled-5091275.20aa05c1cd22fd058e8c68ce58f5a302.gif?f1696187439",
    ),
},

{
    "#url"     : "https://www.newgrounds.com/art/view/zedrinbot/nazrin-tanlines",
    "#comment" : "extra files in 'art-image-row' elements - native PNG files (#4642)",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#urls"    : (
        "https://art.ngfiles.com/images/5009000/5009916_14628_zedrinbot_nazrin-tanlines.265f7b6beec5855a349e2646e90cbc01.png?f1695698131",
        "https://art.ngfiles.com/images/5009000/5009916_14632_zedrinbot_nazrin-tanlines.40bd62fbf5875806cda6b004b348114a.png?f1695698148",
        "https://art.ngfiles.com/images/5009000/5009916_14634_zedrinbot_nazrin-tanlines.40bd62fbf5875806cda6b004b348114a.png?f1695698148",
        "https://art.ngfiles.com/images/5009000/5009916_14633_zedrinbot_nazrin-tanlines.40bd62fbf5875806cda6b004b348114a.png?f1695698148",
        "https://art.ngfiles.com/images/5009000/5009916_14635_zedrinbot_nazrin-tanlines.6a7aa4fd63e5f8077ad29314568246cc.png?f1695698149",
        "https://art.ngfiles.com/images/5009000/5009916_14636_zedrinbot_nazrin-tanlines.6a7aa4fd63e5f8077ad29314568246cc.png?f1695698149",
    ),
},

{
    "#url"     : "https://www.newgrounds.com/art/view/kekiiro/red",
    "#comment" : "'adult' rated (#2456)",
    "#category": ("", "newgrounds", "image"),
    "#class"   : newgrounds.NewgroundsImageExtractor,
    "#options" : {"username": None},
    "#count"   : 0,
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/595355",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#pattern" : r"https://uploads\.ungrounded\.net/alternate/564000/564957_alternate_31\.mp4\?1359712249",

    "artist"     : [
        "kickinthehead",
        "danpaladin",
        "tomfulp",
    ],
    "comment"    : r"re:My fan trailer for Alien Hominid HD!",
    "date"       : "dt:2013-02-01 09:50:49",
    "description": "Fan trailer for Alien Hominid HD!",
    "favorites"  : int,
    "filename"   : "564957_alternate_31",
    "index"      : 595355,
    "rating"     : "e",
    "score"      : float,
    "tags"       : [
        "alienhominid",
        "trailer",
    ],
    "title"      : "Alien Hominid Fan Trailer",
    "type"       : "movie",
    "user"       : "kickinthehead",
},

{
    "#url"     : "https://www.newgrounds.com/audio/listen/609768",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#sha1_url": "f4c5490ae559a3b05e46821bb7ee834f93a43c95",

    "artist"     : [
        "zj",
        "tomfulp",
    ],
    "comment"    : r"""re:RECORDED 12-09-2014

From The ZJ "Late """,
    "date"       : "dt:2015-02-23 19:31:59",
    "description": "From The ZJ Report Show!",
    "favorites"  : int,
    "index"      : 609768,
    "rating"     : "",
    "score"      : float,
    "tags"       : [
        "fulp",
        "interview",
        "tom",
        "zj",
    ],
    "title"      : "ZJ Interviews Tom Fulp!",
    "type"       : "music.song",
    "user"       : "zj",
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/161181/format/flash",
    "#comment" : "flash animation (#1257)",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#pattern" : r"https://uploads\.ungrounded\.net/161000/161181_ddautta_mask__550x281_\.swf\?f1081628129",

    "type": "movie",
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/758545",
    "#comment" : "format selection (#1729)",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#options" : {"format": "720p"},
    "#pattern" : r"https://uploads\.ungrounded\.net/alternate/1482000/1482860_alternate_102516\.720p\.mp4\?\d+",
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/717744",
    "#comment" : "'adult' rated (#2456)",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#options" : {"username": None},
    "#count"   : 1,
},

{
    "#url"     : "https://www.newgrounds.com/portal/view/829032",
    "#comment" : "flash game",
    "#category": ("", "newgrounds", "media"),
    "#class"   : newgrounds.NewgroundsMediaExtractor,
    "#pattern" : r"https://uploads\.ungrounded\.net/829000/829032_picovsbeardx\.swf\?f1641968445",
    "#range"   : "1",

    "artist"     : [
        "dungeonation",
        "carpetbakery",
        "animalspeakandrews",
        "bill",
        "chipollo",
        "dylz49",
        "gappyshamp",
        "pinktophat",
        "rad",
        "shapeshiftingblob",
        "tomfulp",
        "voicesbycorey",
        "psychogoldfish",
    ],
    "comment"    : r"re:The children are expendable. Take out the ",
    "date"       : "dt:2022-01-10 23:00:57",
    "description": "Bloodshed in The Big House that Blew...again!",
    "favorites"  : int,
    "index"      : 829032,
    "post_url"   : "https://www.newgrounds.com/portal/view/829032",
    "rating"     : "m",
    "score"      : float,
    "tags"       : [
        "assassin",
        "boyfriend",
        "darnell",
        "nene",
        "pico",
        "picos-school",
    ],
    "title"      : "PICO VS BEAR DX",
    "type"       : "game",
    "url"        : "https://uploads.ungrounded.net/829000/829032_picovsbeardx.swf?f1641968445",
},

{
    "#url"     : "https://tomfulp.newgrounds.com/art",
    "#category": ("", "newgrounds", "art"),
    "#class"   : newgrounds.NewgroundsArtExtractor,
    "#pattern" : newgrounds.NewgroundsImageExtractor.pattern,
    "#count"   : ">= 3",
},

{
    "#url"     : "https://tomfulp.newgrounds.com/audio",
    "#category": ("", "newgrounds", "audio"),
    "#class"   : newgrounds.NewgroundsAudioExtractor,
    "#pattern" : r"https://audio.ngfiles.com/\d+/\d+_.+\.mp3",
    "#count"   : ">= 4",
},

{
    "#url"     : "https://tomfulp.newgrounds.com/movies",
    "#category": ("", "newgrounds", "movies"),
    "#class"   : newgrounds.NewgroundsMoviesExtractor,
    "#pattern" : r"https://uploads.ungrounded.net(/alternate)?/\d+/\d+_.+",
    "#range"   : "1-10",
    "#count"   : 10,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/games",
    "#category": ("", "newgrounds", "games"),
    "#class"   : newgrounds.NewgroundsGamesExtractor,
    "#pattern" : r"https://uploads.ungrounded.net(/alternate)?/\d+/\d+_.+",
    "#range"   : "1-10",
    "#count"   : 10,
},

{
    "#url"     : "https://tomfulp.newgrounds.com",
    "#category": ("", "newgrounds", "user"),
    "#class"   : newgrounds.NewgroundsUserExtractor,
    "#pattern" : "https://tomfulp.newgrounds.com/art$",
},

{
    "#url"     : "https://tomfulp.newgrounds.com",
    "#category": ("", "newgrounds", "user"),
    "#class"   : newgrounds.NewgroundsUserExtractor,
    "#options" : {"include": "all"},
    "#pattern" : "https://tomfulp.newgrounds.com/(art|audio|movies)$",
    "#count"   : 3,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/art",
    "#category": ("", "newgrounds", "favorite"),
    "#class"   : newgrounds.NewgroundsFavoriteExtractor,
    "#range"   : "1-10",
    "#count"   : ">= 10",
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/audio",
    "#category": ("", "newgrounds", "favorite"),
    "#class"   : newgrounds.NewgroundsFavoriteExtractor,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/movies",
    "#category": ("", "newgrounds", "favorite"),
    "#class"   : newgrounds.NewgroundsFavoriteExtractor,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/",
    "#category": ("", "newgrounds", "favorite"),
    "#class"   : newgrounds.NewgroundsFavoriteExtractor,
},

{
    "#url"     : "https://tomfulp.newgrounds.com/favorites/following",
    "#category": ("", "newgrounds", "following"),
    "#class"   : newgrounds.NewgroundsFollowingExtractor,
    "#pattern" : newgrounds.NewgroundsUserExtractor.pattern,
    "#range"   : "76-125",
    "#count"   : 50,
},

{
    "#url"     : "https://www.newgrounds.com/search/conduct/art?terms=tree",
    "#category": ("", "newgrounds", "search"),
    "#class"   : newgrounds.NewgroundsSearchExtractor,
    "#pattern" : newgrounds.NewgroundsImageExtractor.pattern,
    "#range"   : "1-10",
    "#count"   : 10,

    "search_tags": "tree",
},

{
    "#url"     : "https://www.newgrounds.com/search/conduct/movies?terms=tree",
    "#category": ("", "newgrounds", "search"),
    "#class"   : newgrounds.NewgroundsSearchExtractor,
    "#pattern" : r"https://uploads.ungrounded.net(/alternate)?/\d+/\d+",
    "#range"   : "1-10",
    "#count"   : 10,
},

{
    "#url"     : "https://www.newgrounds.com/search/conduct/audio?advanced=1&terms=tree+green+nature&match=tdtu&genre=5&suitabilities=e%2Cm",
    "#category": ("", "newgrounds", "search"),
    "#class"   : newgrounds.NewgroundsSearchExtractor,
},

)
