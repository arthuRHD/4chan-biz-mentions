#!/usr/bin/python3
from requests import get
import sys


def find_mentions(word: str):
    catalog = get("https://a.4cdn.org/biz/catalog.json").json()
    word_count = 0
    for page in catalog:
        for thread in page['threads']:
            if "com" in thread:
                if word in thread['com'] or word.upper() in thread['com']:
                    word_count += 1
            if "last_replies" in thread:
                for replies in thread['last_replies']:
                    if "com" in replies:
                        if word in replies['com'] or word.upper() in replies['com']:
                            word_count += 1
    return word_count

if __name__ == '__main__':
    try:
        [print(f"{k} mentionned {v} times") for k, v in sorted({str(arg): find_mentions(str(arg)) for arg in sys.argv[1:]}.items(), key=lambda item: item[1], reverse=True)]
    except IndexError:
        print("No words were provided as arguments")