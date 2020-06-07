# SpigotMC_Scraper
Collections of tools used to scrape the SpigotMC forum https://www.spigotmc.org/

# forum-page-json-parser.py

    Parse a page of the forum into a JSON string.
    usage: forum-page-json-parser.py [-h] -i INPUT_FILE_NAME [-o OUTPUT_FILE_NAME]
                                     [-O] [-ji JSON_DUMP_INDENT]

    Parse a spigotmc forum page into a JSON string.

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT_FILE_NAME    File name of the input html file
      -o OUTPUT_FILE_NAME   File name of the output file
      -O                    Print the output
      -ji JSON_DUMP_INDENT  Set the identation of dumped json string (-1 for no
                            indentation). Default: 2

Input is the file name of a file containing html contents of a page of the forum, obtained by browsing a page (e.g. `https://www.spigotmc.org/forums/spigot-plugin-development.52/`) and right-click -> `Save as...` or `View page source` (Chrome), or with an http client.

Output a JSON list with the following fields (for example):

    [{
      "thread-id": 443789,
      "title": "How to detect items dropped into the void?",
      "link": "threads/how-to-detect-items-dropped-into-the-void.443789/",
      "author": "Big_Scary",
      "replies": 2,
      "views:": 10,
      "lastreply": {
        "user": "KerchooK",
        "time": {
          "timestamp": 1591499413,        # Timestamp directly read from HTML. Does not always present.
          "datestring": "Jun 6, 2020",
          "timestring": "11:10 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591495341,          # Timestamp directly read from HTML. Does not always present.
        "datestring": "Jun 6, 2020",
        "timestring": "10:02 PM"          # Does not always present.
      }
    },
    {
      "thread-id": 443078,
      "title": "Name tag colors scoreboard team",
      "link": "threads/name-tag-colors-scoreboard-team.443078/",
      "author": "Extremelyd1",
      "replies": 6,
      ...
    }]

<details>
  <summary>Output Example</summary>

  ```
  [
    {
      "thread-id": 278876,
      "title": "Beginner Programming Mistakes and Why You're Making Them",
      "link": "threads/beginner-programming-mistakes-and-why-youre-making-them.278876/",
      "author": "Choco",
      "replies": 74,
      "views:": 19038,
      "lastreply": {
        "user": "garbagemule",
        "time": {
          "datestring": "May 25, 2020"
        }
      },
      "postdate": {
        "datestring": "Oct 14, 2017"
      }
    },
    {
      "thread-id": 72946,
      "title": "[READ ME] For everyone asking questions on here.",
      "link": "threads/read-me-for-everyone-asking-questions-on-here.72946/",
      "author": "SubSide",
      "replies": 105,
      "views:": 45371,
      "lastreply": {
        "user": "Arttie",
        "time": {
          "datestring": "Apr 12, 2020"
        }
      },
      "postdate": {
        "datestring": "Jun 19, 2015"
      }
    },
    {
      "thread-id": 64953,
      "title": "Attention Developers: Opportunity to contribute to Spigot / build your portfolio!",
      "link": "threads/attention-developers-opportunity-to-contribute-to-spigot-build-your-portfolio.64953/",
      "author": "jflory7",
      "replies": 65,
      "views:": 33249,
      "lastreply": {
        "user": "Stef",
        "time": {
          "datestring": "May 24, 2018"
        }
      },
      "postdate": {
        "datestring": "May 8, 2015"
      }
    },
    {
      "thread-id": 33587,
      "title": "[READ ME] Why can I NOT post a premium resource?",
      "link": "threads/read-me-why-can-i-not-post-a-premium-resource.33587/",
      "author": "jflory7",
      "replies": 0,
      "views:": 21091,
      "lastreply": {
        "user": "jflory7",
        "time": {
          "datestring": "Oct 26, 2014"
        }
      },
      "postdate": {
        "datestring": "Oct 26, 2014"
      }
    },
    {
      "thread-id": 20981,
      "title": "[Read Me] Don't try to hire developers here, use the Services & Recruitment forum",
      "link": "threads/read-me-dont-try-to-hire-developers-here-use-the-services-recruitment-forum.20981/",
      "author": "Thinkofdeath",
      "replies": 0,
      "views:": 17679,
      "lastreply": {
        "user": "Thinkofdeath",
        "time": {
          "datestring": "Jun 13, 2014"
        }
      },
      "postdate": {
        "datestring": "Jun 13, 2014"
      }
    },
    {
      "thread-id": 443789,
      "title": "How to detect items dropped into the void?",
      "link": "threads/how-to-detect-items-dropped-into-the-void.443789/",
      "author": "Big_Scary",
      "replies": 2,
      "views:": 10,
      "lastreply": {
        "user": "KerchooK",
        "time": {
          "timestamp": 1591499413,
          "datestring": "Jun 6, 2020",
          "timestring": "11:10 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591495341,
        "datestring": "Jun 6, 2020",
        "timestring": "10:02 PM"
      }
    },
    {
      "thread-id": 443078,
      "title": "Name tag colors scoreboard team",
      "link": "threads/name-tag-colors-scoreboard-team.443078/",
      "author": "Extremelyd1",
      "replies": 6,
      "views:": 56,
      "lastreply": {
        "user": "KingAlterIV",
        "time": {
          "timestamp": 1591499230,
          "datestring": "Jun 6, 2020",
          "timestring": "11:07 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591213002,
        "datestring": "Jun 3, 2020",
        "timestring": "3:36 PM"
      }
    },
    {
      "thread-id": 443790,
      "title": "Support Multiple Versions - Advanced Resource",
      "link": "threads/support-multiple-versions-advanced-resource.443790/",
      "author": "FlexKawai",
      "replies": 2,
      "views:": 32,
      "lastreply": {
        "user": "DiegoNighty",
        "time": {
          "timestamp": 1591496514,
          "datestring": "Jun 6, 2020",
          "timestring": "10:21 PM"
        }
      },
      "tag": "Resource",
      "posttime": {
        "timestamp": 1591495848,
        "datestring": "Jun 6, 2020",
        "timestring": "10:10 PM"
      }
    },
    {
      "thread-id": 443735,
      "title": "Events for a specific player",
      "link": "threads/events-for-a-specific-player.443735/",
      "author": "DasGandlaf",
      "replies": 13,
      "views:": 104,
      "lastreply": {
        "user": "DasGandlaf",
        "time": {
          "timestamp": 1591493013,
          "datestring": "Jun 6, 2020",
          "timestring": "9:23 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591476819,
        "datestring": "Jun 6, 2020",
        "timestring": "4:53 PM"
      }
    },
    {
      "thread-id": 443742,
      "title": "Beginner maven help",
      "link": "threads/beginner-maven-help.443742/unread",
      "author": "KerchooK",
      "replies": 6,
      "views:": 60,
      "lastreply": {
        "user": "gyurix",
        "time": {
          "timestamp": 1591492936,
          "datestring": "Jun 6, 2020",
          "timestring": "9:22 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591479003,
        "datestring": "Jun 6, 2020",
        "timestring": "5:30 PM"
      }
    },
    {
      "thread-id": 443783,
      "title": "Skeleton is deprecated",
      "link": "threads/skeleton-is-deprecated.443783/",
      "author": "UnspecifiedUser",
      "replies": 1,
      "views:": 18,
      "lastreply": {
        "user": "UnspecifiedUser",
        "time": {
          "timestamp": 1591492652,
          "datestring": "Jun 6, 2020",
          "timestring": "9:17 PM"
        }
      },
      "tag": "1.12.2",
      "posttime": {
        "timestamp": 1591492440,
        "datestring": "Jun 6, 2020",
        "timestring": "9:14 PM"
      }
    },
    {
      "thread-id": 443711,
      "title": "Create custom anvil recipe (with custom price)",
      "link": "threads/create-custom-anvil-recipe-with-custom-price.443711/",
      "author": "Lockface77",
      "replies": 18,
      "views:": 143,
      "lastreply": {
        "user": "heatseeker0",
        "time": {
          "timestamp": 1591492105,
          "datestring": "Jun 6, 2020",
          "timestring": "9:08 PM"
        }
      },
      "tag": "1.8.8",
      "posttime": {
        "timestamp": 1591468515,
        "datestring": "Jun 6, 2020",
        "timestring": "2:35 PM"
      }
    },
    {
      "thread-id": 395868,
      "title": "Methods for changing massive amount of blocks (Up to 14M blocks/s)",
      "link": "threads/methods-for-changing-massive-amount-of-blocks-up-to-14m-blocks-s.395868/",
      "author": "NascentNova",
      "replies": 26,
      "views:": 3173,
      "lastreply": {
        "user": "7rory768",
        "time": {
          "timestamp": 1591491894,
          "datestring": "Jun 6, 2020",
          "timestring": "9:04 PM"
        }
      },
      "tag": "Resource",
      "postdate": {
        "datestring": "Sep 14, 2019"
      }
    },
    {
      "thread-id": 443539,
      "title": "Scoreboard below name",
      "link": "threads/scoreboard-below-name.443539/",
      "author": "wand555",
      "replies": 3,
      "views:": 35,
      "lastreply": {
        "user": "gyurix",
        "time": {
          "timestamp": 1591491601,
          "datestring": "Jun 6, 2020",
          "timestring": "9:00 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591389452,
        "datestring": "Jun 5, 2020",
        "timestring": "4:37 PM"
      }
    },
    {
      "thread-id": 443751,
      "title": "[Java] Organising a list of strings",
      "link": "threads/java-organising-a-list-of-strings.443751/",
      "author": "HarleySwtfus",
      "replies": 6,
      "views:": 73,
      "lastreply": {
        "user": "HarleySwtfus",
        "time": {
          "timestamp": 1591490386,
          "datestring": "Jun 6, 2020",
          "timestring": "8:39 PM"
        }
      },
      "tag": "Solved",
      "posttime": {
        "timestamp": 1591482945,
        "datestring": "Jun 6, 2020",
        "timestring": "6:35 PM"
      }
    },
    {
      "thread-id": 443760,
      "title": "Zombies with texture and hitbox of a random block",
      "link": "threads/zombies-with-texture-and-hitbox-of-a-random-block.443760/",
      "author": "DasGandlaf",
      "replies": 4,
      "views:": 43,
      "lastreply": {
        "user": "DasGandlaf",
        "time": {
          "timestamp": 1591488503,
          "datestring": "Jun 6, 2020",
          "timestring": "8:08 PM"
        }
      },
      "tag": "Solved",
      "posttime": {
        "timestamp": 1591485817,
        "datestring": "Jun 6, 2020",
        "timestring": "7:23 PM"
      }
    },
    {
      "thread-id": 443749,
      "title": "Right clicking an entity triggers left click.",
      "link": "threads/right-clicking-an-entity-triggers-left-click.443749/",
      "author": "NikosMaster",
      "replies": 1,
      "views:": 32,
      "lastreply": {
        "user": "GodCipher",
        "time": {
          "timestamp": 1591485365,
          "datestring": "Jun 6, 2020",
          "timestring": "7:16 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591482337,
        "datestring": "Jun 6, 2020",
        "timestring": "6:25 PM"
      }
    },
    {
      "thread-id": 443737,
      "title": "Getting a bunch of errors",
      "link": "threads/getting-a-bunch-of-errors.443737/",
      "author": "SadMess",
      "replies": 6,
      "views:": 69,
      "lastreply": {
        "user": "ironinventor",
        "time": {
          "timestamp": 1591485043,
          "datestring": "Jun 6, 2020",
          "timestring": "7:10 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591478332,
        "datestring": "Jun 6, 2020",
        "timestring": "5:18 PM"
      }
    },
    {
      "thread-id": 443750,
      "title": "How to check in Seconds how long a Player is in a Custom Inventory?",
      "link": "threads/how-to-check-in-seconds-how-long-a-player-is-in-a-custom-inventory.443750/",
      "author": "xemoti9",
      "replies": 3,
      "views:": 47,
      "lastreply": {
        "user": "DiegoNighty",
        "time": {
          "timestamp": 1591482873,
          "datestring": "Jun 6, 2020",
          "timestring": "6:34 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591482360,
        "datestring": "Jun 6, 2020",
        "timestring": "6:26 PM"
      }
    },
    {
      "thread-id": 443714,
      "title": "Performance of Bungee messaging channels",
      "link": "threads/performance-of-bungee-messaging-channels.443714/",
      "author": "derteufelqwe",
      "replies": 5,
      "views:": 50,
      "lastreply": {
        "user": "heatseeker0",
        "time": {
          "timestamp": 1591478353,
          "datestring": "Jun 6, 2020",
          "timestring": "5:19 PM"
        }
      },
      "tag": "1.12.2",
      "posttime": {
        "timestamp": 1591470072,
        "datestring": "Jun 6, 2020",
        "timestring": "3:01 PM"
      }
    },
    {
      "thread-id": 442466,
      "title": "Hashmap as global variable (static?)",
      "link": "threads/hashmap-as-global-variable-static.442466/unread",
      "author": "ORENYT",
      "replies": 74,
      "views:": 673,
      "lastreply": {
        "user": "DarkSeraphim",
        "time": {
          "timestamp": 1591477401,
          "datestring": "Jun 6, 2020",
          "timestring": "5:03 PM"
        }
      },
      "tag": "Solved",
      "posttime": {
        "timestamp": 1590964458,
        "datestring": "May 31, 2020",
        "timestring": "6:34 PM"
      }
    },
    {
      "thread-id": 443727,
      "title": "Problems with ItemBuilder",
      "link": "threads/problems-with-itembuilder.443727/",
      "author": ".serious",
      "replies": 10,
      "views:": 79,
      "lastreply": {
        "user": ".serious",
        "time": {
          "timestamp": 1591477161,
          "datestring": "Jun 6, 2020",
          "timestring": "4:59 PM"
        }
      },
      "tag": "1.8.8",
      "posttime": {
        "timestamp": 1591475158,
        "datestring": "Jun 6, 2020",
        "timestring": "4:25 PM"
      }
    },
    {
      "thread-id": 443723,
      "title": "Multiverse-Core map will not be found.",
      "link": "threads/multiverse-core-map-will-not-be-found.443723/",
      "author": "DephtChaos",
      "replies": 1,
      "views:": 42,
      "lastreply": {
        "user": "DephtChaos",
        "time": {
          "timestamp": 1591474914,
          "datestring": "Jun 6, 2020",
          "timestring": "4:21 PM"
        }
      },
      "tag": "1.12.2",
      "posttime": {
        "timestamp": 1591472538,
        "datestring": "Jun 6, 2020",
        "timestring": "3:42 PM"
      }
    },
    {
      "thread-id": 440467,
      "title": "Custom Popup \"Announcements\"",
      "link": "threads/custom-popup-announcements.440467/",
      "author": "JadedDragoon",
      "replies": 1,
      "views:": 74,
      "lastreply": {
        "user": "Nowaha",
        "time": {
          "timestamp": 1591474519,
          "datestring": "Jun 6, 2020",
          "timestring": "4:15 PM"
        }
      },
      "tag": "1.15.2",
      "postdate": {
        "datestring": "May 22, 2020"
      }
    },
    {
      "thread-id": 442475,
      "title": "Give Permissions To A Player Using Skript",
      "link": "threads/give-permissions-to-a-player-using-skript.442475/",
      "author": "CharlieCharlie",
      "replies": 1,
      "views:": 22,
      "lastreply": {
        "user": "Nowaha",
        "time": {
          "timestamp": 1591474222,
          "datestring": "Jun 6, 2020",
          "timestring": "4:10 PM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1590968966,
        "datestring": "May 31, 2020",
        "timestring": "7:49 PM"
      }
    }
  ]
  ```
</details>
