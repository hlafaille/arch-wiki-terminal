import requests as requests

from html_parser import table_of_contents, header, optional_features_list, get_section

class PageHandler:
    def __init__(self):
        self.page = None
        self.sections = {}

    def user_input(self):
        # Get the user input
        user_input = input("search> ")

        print("searching...")

        # Get the HTML of the page
        self.page = requests.get("https://wiki.archlinux.org/index.php?search={0}".format(user_input)).text

        self.root_page()

    def root_page(self,):
        # Get the various elements from the page
        header_text = header.ParseHeader(self.page)
        body_list = optional_features_list.BodyList(self.page).parse()
        self.sections = table_of_contents.ParseTableOfContents(self.page).parse()

        if not header_text.parse() == "Search results":
            print("-------------------------------")
            # Print the page out to stdout
            print(header_text.parse())
            if body_list:
                print("-------------------------------")
                for bullet in body_list:
                    print("- {0}".format(bullet))
            print("-------------------------------")
            for content in self.sections:
                if content["level"].count(".") == 1:
                    print("   {0} --- {1}".format(content["level"], content["text"]))
                elif content["level"].count(".") == 2:
                    print("      {0} --- {1}".format(content["level"], content["text"]))
                else:
                    print("{0} --- {1}".format(content["level"], content["text"]))
            print("-------------------------------")
            self.get_section()
        else:
            print("nothing was found")
            self.user_input()

    def get_section(self):
        # Ask the user which section they want
        section = input("section> ")

        # If the user wants to re-search something
        if section == "e":
            self.user_input()
        else:
            specific_section = get_section.GetSection(self.page, self.sections, section)
            specific_section.parse()
if __name__ == "__main__":
    page_handler = PageHandler()
    page_handler.user_input()