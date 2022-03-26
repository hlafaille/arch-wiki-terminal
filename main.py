import re
import sys

import requests
from bs4 import BeautifulSoup
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

    # check if theres any results found
    results_query_check = soup.find("p", {"class": "mw-search-nonefound"})
    if not results_query_check:
        # get and print the header
        main_header = soup.find("h1", {"class": "firstHeading"})
        print(util.color_header(main_header.text))
        print("--------------------")

        # get the main content
        main_content = soup.find("main", {"id": "content"})

        # get the big boy paragraph (if there is one)
        try:
            big_boy_paragraph = soup.find("dd")
            print(big_boy_paragraph.text)
            print("--------------------")
        except AttributeError:
            # there's probably a <p>/ list here then..
            try:
                tiny_boy_description = main_content.find("div", {"class": "archwiki-template-meta-related-articles-start"}).find_next_sibling("p")
                print(tiny_boy_description.text)
                tiny_boy_list = tiny_boy_description.find_next_sibling("ul")

                temp = []
                for x in tiny_boy_list.children:
                    temp.append(x.text.replace("\n", ""))

                for x in temp:
                    if not x == "":
                        print("- {0} ".format(x))
                print("--------------------")
            except AttributeError:
                pass

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
        try:
            next_tag = page_headers[user_input - 1].find_all_next(["p", "span", "div", "pre", "li", "a"])

            for x in next_tag:
                try:
                    if x.name == "span" and x.text == page_headers[user_input].text:
                        break
                except IndexError:
                    pass
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

                        # if this is a note box
                        elif x.name == "div" and "archwiki-template-box-note" in x["class"]:
                            print(util.color_note_box(x.text))

                        # if this is a note box
                        elif x.name == "div" and "archwiki-template-box-tip" in x["class"]:
                            print(util.color_tip_box(x.text))

                        # if this is a codeblock
                        elif x.name == "pre":
                            print(util.color_codeblock(x.text))

                        # if this is a list element
                        elif x.name == "li":
                            print("- {0}".format(x.text))

                        # if this is a URL
                        elif x.name == "a":
                            if "http" in x["href"]:
                                print(util.color_url("{0} - {1}".format(x.text, x["href"])))

                        # if this is a standard paragraph
                        elif x.name == "p":
                            print(re.sub('\\s+', ' ', x.text))

                    except KeyError:
                        pass
        except IndexError:
            print("selection out of range")

    else:
        print("no results")
