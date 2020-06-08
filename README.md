# SpigotMC_Scraper
Collections of tools used to scrape the SpigotMC forum https://www.spigotmc.org/

# forum-page-json-parser.py

    usage: forum_page_json_parser.py [-h] -i INPUT_FILE_NAME [-o OUTPUT_FILE_NAME]
                                     [-O] [-ji JSON_DUMP_INDENT] [-is]

    Parse a spigotmc forum page into a JSON string.

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT_FILE_NAME    File name of the input html file
      -o OUTPUT_FILE_NAME   File name of the output file
      -O                    Print the output
      -ji JSON_DUMP_INDENT  Set the identation of dumped json string (-1 for no
                            indentation). Default: 2
      -is, --ignore-sticky  Ignore sticky threads. Off by default.

Input is the file name of a file containing html contents of a page of the forum, obtained by browsing a page (e.g. `https://www.spigotmc.org/forums/spigot-plugin-development.52/`) and right-click -> `Save as...` or `View page source` (Chrome), or with an http client.

Output a JSON list with the following fields (for example):

    [{
      "thread-id": 443789,
      "title": "How to detect items dropped into the void?",
      "link": "threads/how-to-detect-items-dropped-into-the-void.443789/",
      "author": "Big_Scary",
      "replies": 4,
      "views:": 73,
      "lastreply": {
        "user": "Big_Scary",
        "time": {
          "timestamp": 1591545222,        # Timestamp directly read from HTML. Does not always present.
          "datestring": "Jun 7, 2020",
          "timestring": "11:53 AM"
        }
      },
      "tag": "1.15.2",
      "posttime": {
        "timestamp": 1591495341,          # Timestamp directly read from HTML. Does not always present.
        "datestring": "Jun 6, 2020",
        "timestring": "10:02 PM"          # Does not always present.
      },
      "sticky": false,
      "locked": false
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
      "thread-id": 371050,
      "title": "APRENDER A CREAR PLUGINS",
      "link": "threads/aprender-a-crear-plugins.371050/",
      "author": "Anokilor",
      "replies": 7,
      "views:": 1042,
      "lastreply": {
        "user": "NascentNova",
        "time": {
          "timestamp": 1591593819,
          "datestring": "Jun 8, 2020",
          "timestring": "1:23 AM"
        }
      },
      "postdate": {
        "datestring": "May 2, 2019"
      },
      "sticky": false,
      "locked": false
    },
    {
      "thread-id": 444011,
      "title": "Crafting with ShapedRecipe",
      "link": "threads/crafting-with-shapedrecipe.444011/",
      "author": "Wilsoon",
      "replies": 2,
      "views:": 46,
      "lastreply": {
        "user": "Wilsoon",
        "time": {
          "timestamp": 1591593695,
          "datestring": "Jun 8, 2020",
          "timestring": "1:21 AM"
        }
      },
      "tag": "Solved",
      "posttime": {
        "timestamp": 1591588371,
        "datestring": "Jun 7, 2020",
        "timestring": "11:52 PM"
      },
      "sticky": false,
      "locked": true
    },
    {
      "thread-id": 443962,
      "title": "Syncing & saving data across servers on a network",
      "link": "threads/syncing-saving-data-across-servers-on-a-network.443962/",
      "author": "Reparo",
      "replies": 2,
      "views:": 62,
      "lastreply": {
        "user": "UniverseCraft",
        "time": {
          "timestamp": 1591588710,
          "datestring": "Jun 7, 2020",
          "timestring": "11:58 PM"
        }
      },
      "tag": "1.12.2",
      "posttime": {
        "timestamp": 1591561753,
        "datestring": "Jun 7, 2020",
        "timestring": "4:29 PM"
      },
      "sticky": false,
      "locked": false
    },
    ...
  ```
</details>
