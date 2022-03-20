import re

look_for = ["firstHeading"]


class ParseHeader:
    def __init__(self, html):
        self.html = html.split("\n")
        self.header = []

    # Parses out all of our table of contents entries
    def parse(self):
        temp = []
        # Iterate over every line in the HTML
        for line in self.html:

            # Get all table of contents entries
            if any(x in line for x in look_for):
                # Use Regex to filter out HTML tags, we only want stuff between > and <
                temp = re.findall('>(.*?)<', line)

        return temp[0]
