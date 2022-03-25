import os

import requests
from bs4 import BeautifulSoup

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
    #print("user input is {0}, getting next next_element.text until next element text is {1}".format(user_input, page_headers[user_input].text))

    print("--------------------")

    # get all the text between this h2 and the next h2
    next_tag = page_headers[user_input - 1].find_all_next(['p', "span"])

    for x in next_tag:
        if x.name == "span" and x.text == page_headers[user_input].text:
            print("breaking")
            break
        else:
            # if the headline is the same as the selected headline, make it stand out
            if x.name == "span" and x.text == page_headers[user_input - 1]:
                print("-[ {0}".format(x.text))

            elif x.name == "span" and "mw-headline" in x["class"]:
                print("# {0}".format(x.text))