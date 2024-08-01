import json

from nbweb.page import Page
from nbweb.parser import Parser

from urllib.parse import urlparse
from importlib.resources import files


def get_content(url):
    rules = get_rules(url)
    html = Page(url).get()
    content = Parser(rules, html).get()
    return content


def get_rules(url):
    u = urlparse(url)
    json_data = json.loads(files("nbweb").joinpath("data.json").read_text())
    for entry in json_data:
        e = urlparse(entry["url"])
        if u.hostname in e.hostname:
            return entry["rules"]
    raise TypeError("url not supported")
