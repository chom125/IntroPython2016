#!/usr/bin/env python3

class Element:
    tag = "html"
    def __init__(self, content=None):
        self.content = []
        if content is not None:
            self.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, out_file, indent=""):
        out_file.write("<{}>\n".format(self.tag))
        for stuff in self.content:
            out_file.write(stuff+"\n")
        out_file.write("</{}>\n".format(self.tag))

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"
    indent = "    "

class P(Element):
    tag = "p"
    indent = "        "




