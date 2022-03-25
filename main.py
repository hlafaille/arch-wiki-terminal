import os
import re

import requests
from bs4 import BeautifulSoup

import util
from util import Colors

if __name__ == "__main__":
    # ask for search
    user_search = input("search> ")

    # get data from arch wiki
    data = requests.get("https://wiki.archlinux.org/index.php?search={0}".format(user_search))

    # set up beautifulsoup
    soup = BeautifulSoup(data.text, 'html.parser')

    # get and print the header
    main_header = soup.find("h1", {"class": "firstHeading"})
    print(main_header.text)
    print("--------------------")

    # get the main content
    main_content = soup.find("main", {"id": "content"})

    # get the big boy paragraph
    try:
        big_boy_paragraph = soup.find("dd")
        print(big_boy_paragraph.text)
        print("--------------------")
    except AttributeError:
        print("...")

    # get all h2 headings in the main content
    page_headers = main_content.find_all("h2", id=None)

    headers_count = 0
    for header in page_headers:
        if not header.text == "Contents":
            headers_count += 1
            print("[{0}] {1}".format(headers_count, header.text))

    user_input = int(input("> "))
    # print("user input is {0}, getting next next_element.text until next element text is {1}".format(user_input, page_headers[user_input].text))

    print("--------------------")

    # get all the text between this h2 and the next h2
    next_tag = page_headers[user_input - 1].find_all_next(['p', "span", "div", "pre"])

    for x in next_tag:
        if x.name == "span" and x.text == page_headers[user_input].text:
            print("breaking")
            break
        else:
            try:
                # if the headline is the same as the selected headline, make it stand out
                if x.name == "span" and x.text == page_headers[user_input - 1].text:
                    print(util.color_header("-[ {0}".format(x.text)))
                    print(util.color_header("--------------------"))
                    print("")

                # if this is a subheadline, make it stand out a bit less
                elif x.name == "span" and "mw-headline" in x["class"]:
                    print(util.color_subheader("# {0}".format(x.text)))

                # if this is a warning box
                elif x.name == "div" and "archwiki-template-box-warning" in x["class"]:
                    print(util.color_warning_box(x.text))

                # if this is a codeblock
                elif x.name == "pre":
                    print(util.color_codeblock(x.text))

                # if this is a standard paragraph
                elif x.name == "p" and not x.text == "":
                    print(re.sub('\\s+', ' ', x.text))
                    print("")

            except KeyError:
                pass
