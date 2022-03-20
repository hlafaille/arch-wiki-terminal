import requests as requests

from html_parser import table_of_contents, header, optional_features_list, external_text

class PageHandler:
    def __init__(self, page):
        self.page = page

    def root_page(self):
        # Get the various elements from the page
        header_text = header.ParseHeader(self.page)
        body_list = optional_features_list.BodyList(self.page).parse()
        # body_text = external_text.ParseExternalText(page).parse()
        toc = table_of_contents.ParseTableOfContents(self.page)

        # Print the page out to stdout
        print(header_text.parse())
        if body_list:
            print("-------------------------------")
            for bullet in body_list:
                print("- {0}".format(bullet))
        print("-------------------------------")
        for content in toc.parse():
            if content["level"].count(".") == 1:
                print("   {0} --- {1}".format(content["level"], content["text"]))
            elif content["level"].count(".") == 2:
                print("      {0} --- {1}".format(content["level"], content["text"]))
            else:
                print("{0} --- {1}".format(content["level"], content["text"]))
        print("-------------------------------")

if __name__ == "__main__":
    # Get the user input
    user_input = input("search> ")

    print("searching...")

    # Get the HTML of the page
    page = requests.get("https://wiki.archlinux.org/index.php?search={0}".format(user_input)).text

    # Create a page handler, print the root page
    page_handler = PageHandler(page)
    PageHandler.root_page()

    # Ask the user which section they want
    section = input("section> ")