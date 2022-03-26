import re
import sys

import requests
from bs4 import BeautifulSoup

import chapter_body
import util

if __name__ == "__main__":
    try:
        # if there was no argument on exec
        if not sys.argv[1]:
            # ask for search
            user_search = input("search> ")

            # get data from arch wiki
            data = requests.get("https://wiki.archlinux.org/index.php?search={0}".format(user_search))
        # if there is an argument on exec
        else:
            # get data from arch wiki
            data = requests.get("https://wiki.archlinux.org/index.php?search={0}".format(sys.argv[1]))

    except IndexError:
        # ask for search
        user_search = input("search> ")

        # get data from arch wiki
        data = requests.get("https://wiki.archlinux.org/index.php?search={0}".format(user_search))

    # set up beautifulsoup
    soup = BeautifulSoup(data.text, 'html.parser')

    chapter_body.chapter_selection(soup)
