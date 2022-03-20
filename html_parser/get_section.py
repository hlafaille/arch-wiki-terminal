import re

from bs4 import BeautifulSoup

look_for = ["<p>"]

class GetSection:
    def __init__(self, html, section_dictionary, requested_section):
        self.html = html
        self.section_dictionary = section_dictionary
        self.requested_action = requested_section

    # Parses out all of our table of contents entries
    def parse(self):
        soup = BeautifulSoup(self.html, 'html.parser')

        '''container = soup.find_all(["span", "p"])
        for x in container:
            print(x.get_text())'''

        for s in soup.find_all(["span", "p"]):
            s, s.findParent(), s.findParent().findNextSibling()
            print(s)

    def get_action_text(self):
        # Check if the requested action is in the table of contents
        for content in self.section_dictionary:
            if content["level"] == self.requested_action:
                return content["text"]
