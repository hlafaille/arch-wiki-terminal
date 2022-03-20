import re

look_for = ["<li>"]

class BodyList:
    def __init__(self, html):
        self.html = html.split("\n")
        self.body_list = []

    # Parses out all of our table of contents entries
    def parse(self):
        temp = []
        ignore_related_articles = False

        # Iterate over every line in the HTML
        for line in self.html:

            # Ignore the related articles
            if "<div" in line and "archwiki-template-meta-related-articles-start" in line:
                ignore_related_articles = True

            # If we've reached the end of related articles
            elif "</div>" in line:
                ignore_related_articles = False

            if not ignore_related_articles:
                # Use Regex to filter out HTML tags, we only want stuff between > and <
                temp = re.findall('>(.*?)<', line)

                temp = list(filter(None, temp))

                # Get all the paragraph tags
                if any(x in line for x in look_for):
                    self.body_list.append(temp[0])

            # Ensure that this is the end of the body list
            if "<div" in line and "toc" in line:
                break

        return self.body_list

