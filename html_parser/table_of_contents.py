import re

look_for = ["toclevel"]

class ParseTableOfContents:
    def __init__(self, html):
        self.html = html.split("\n")
        self.toc = []

    # Parses out all of our table of contents entries
    def parse(self):
        # Iterate over every line in the HTML
        for line in self.html:

            # Get all table of contents entries
            if any(x in line for x in look_for):

                # Use Regex to filter out HTML tags, we only want stuff between > and <
                temp = re.findall('>(.*?)<', line)

                # Append the table of contents for this page to a dictionary
                self.toc.append({"level": temp[2], "text": temp[4]})

        return self.toc
