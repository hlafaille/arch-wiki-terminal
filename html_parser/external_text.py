import re

look_for = ["<p>"]

class ParseExternalText:
    def __init__(self, html):
        self.html = html.split("\n")
        self.body_text = False
    # Parses out all of our table of contents entries
    def parse(self):
        temp = []

        # Iterate over every line in the HTML
        for line in self.html:
            if 'archwiki-template-meta-related-articles-start' in line:
                self.body_text = True

            if self.body_text:
                print(line)

            if '</p>' in line:
                self.body_text = False

