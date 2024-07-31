from importlib.resources import files
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
        for key in self.rules:
            data[key] = self._get_content(self.rules[key]["selector"])
        return data

    def _get_content(self, selector):
        elems = self.parser.css(f"{selector}::text").getall()
        if elems is not None and len(elems) > 0:
            return "\n".join(elems)
        return ""

    def _set_rules(self):
        json_text = files("nbweb").joinpath("data.json").read_text()
        self.rules = Selector(text=json_text)
        print(f"rules: {self.rules}")
        self.rules = self.rules.jmespath(f'"{self.website}".rules').get()
        print(f"rules: {self.rules}")
