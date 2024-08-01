import json

from urllib.parse import urlparse

from importlib.resources import files
from parsel import Selector


class Parser:
    def __init__(self, link, html):
        self.link = link
        self.html = html
        self.parser = Selector(text=html)
        self._set_rules()

    def get(self):
        data = {}
        for key in self.rules:
            data[key] = self._get_content(self.rules[key]["selector"])
        return data

    def _get_content(self, selector):
        elems = self.parser.css(selector).getall()
        if elems is not None and len(elems) > 0:
            return "\n".join(elems)
        return ""

    def _set_rules(self):
        o = urlparse(self.link)
        json_data = json.loads(files("nbweb").joinpath("data.json").read_text())

        for entry in json_data:
            e = urlparse(entry["url"])
            print(f"o.hostname: {o.hostname}")
            print(f"e.hostname: {e.hostname}")
            if o.hostname in e.hostname:
                self.rules = entry["rules"]
                print(f"rules: {self.rules}")
                return

        raise TypeError("url not supported")
