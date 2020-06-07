'''
  Parse a spigotmc forum page into a JSON string.
  Author: Nova41 (https://github.com/Nova41)
  Date created: 6/7/2020
  Version: 1.0 (6/7/2020)
'''

import argparse
import sys
import locale
from bs4 import BeautifulSoup
import json

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def parse_thread_list(content, json_dump_indent):
  """Parse a spigotmc forum page into a JSON string.

  Args:
      content: The html string of the page.
      json_dump_indent: The identation of the dumped json string. Set to None for no identation.

  Returns:
      The parsed JSON object with specified indentation.
  """
  threads = []

  soup = BeautifulSoup(content, 'html.parser')
  threads_tag = soup.find('ol', class_='discussionListItems')
  for thread_tag in threads_tag.find_all('li', class_='discussionListItem'):
    # basic data
    tag_main = thread_tag.find('div', class_='main')
    tag_stats = thread_tag.find('div', class_='stats')
    tag_lastpost = thread_tag.find('div', class_='lastPost')
    thread = {
      'thread-id': int(thread_tag['id'].split('-')[1]),
      'title':     tag_main.div.h3.find('a', class_='PreviewTooltip').string,
      'link':      tag_main.div.h3.find('a', class_='PreviewTooltip')['href'],
      'author':    thread_tag['data-author'],
      'replies':   locale.atoi(tag_stats.find('dl', class_='major').find('dd').string),
      'views:':    locale.atoi(tag_stats.find('dl', class_='minor').find('dd').string),
      'lastreply': {
        'user':      tag_lastpost.dl.dt.a.string,
      }
    }

    # if the thread has a tag
    if tag_main.div.h3.find('a', class_='prefixLink') is not None:
      thread['tag'] = tag_main.div.h3.find('a', class_='prefixLink').span.string

    # if the thread has a unix post time
    tag_posterdate = tag_main.div.find('div', class_='secondRow').find('div', class_='posterDate')
    tag_startdate = tag_posterdate.find('span', class_='startDate')
    if tag_startdate.a.abbr is not None:
      thread['posttime'] = {
        'timestamp':  int(tag_startdate.a.abbr['data-time']),
        'datestring': tag_startdate.a.abbr['data-datestring'],
        'timestring': tag_startdate.a.abbr['data-timestring']
      }
    else:
      thread['postdate'] = {
        'datestring': tag_startdate.a.span.string
      }

    # if the thread has a unix reply time
    if tag_lastpost.dl.dd.a.abbr is not None:
      thread['lastreply']['time'] = {
        'timestamp':  int(tag_lastpost.dl.dd.a.abbr['data-time']),
        'datestring': tag_lastpost.dl.dd.a.abbr['data-datestring'],
        'timestring': tag_lastpost.dl.dd.a.abbr['data-timestring']
      }
    else:
      thread['lastreply']['time'] = {
        'datestring': tag_lastpost.dl.dd.a.span.string,
        'timestring': tag_lastpost.dl.dd.a.span['title'].split(' at ')[1]
      }

    threads.append(thread)

  return json.dumps(threads, indent=json_dump_indent)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Parse a spigotmc forum page into a JSON string.")
  parser.add_argument('-i', required=True, dest='input_file_name', help="File name of the input html file")
  parser.add_argument('-o', dest='output_file_name', help="File name of the output file")
  parser.add_argument('-O', dest='print_output', action='store_true', help="Print the output")
  parser.add_argument('-ji', default=2, type=int, dest='json_dump_indent', help="Set the identation of dumped json string (-1 for no indentation). Default: 2")
  if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
  args = parser.parse_args()

  try:
    input_file = open(args.input_file_name, 'r')
  except IOError:
    print("Cannot find or open input file '%s'" % args.input_file_name)
    sys.exit(1)

  with input_file:
    if (args.json_dump_indent >= 0):
      parsed_json_string = parse_thread_list(input_file.read(), args.json_dump_indent)
    else:
      parsed_json_string = parse_thread_list(input_file.read(), None)

  if args.print_output:
    print(parsed_json_string)

  if args.output_file_name is not None:
    try:
      output_file = open(args.output_file_name, 'w')
    except IOError:
      print("Cannot find or open output file '%s'" % args.input_file_name)
      sys.exit(1)

    with output_file:
      output_file.write(parsed_json_string)