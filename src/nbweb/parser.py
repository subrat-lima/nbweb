from parsel import Selector
from nbweb.page import Page


class Parser:
    def __init__(self, website, html):
        self.website = website
        self.html = html
        self.parser = Selector(text=html)
        self._set_rules()

    def get(self):
        data = {}
        for key in self.rules["article"]:
            data[key] = _get_content(self.rules["article"][key]["selector"])
        return data

    def _get_content(self, selector):
        elems = self.parser.css(selector).getall()
        if elems is not None and len(elems) > 0:
            return "\n".join(elems)
        return ""

    def _set_rules(self):
        with open("data.json") as f:
            json_text = f.read()
        self.rules = Selector(text=json_text).jmespath(self.website).get()
