import json
from importlib.resources import files
from urllib.parse import urlparse

from nbweb.page import Page
from nbweb.parser import Parser


def get_content(url: str, return_type: str):
    rules = get_rules(url, "rules")
    html = Page(url).get()
    content = Parser(rules, html).get()
    if return_type == "txt":
        return json2txt(content)
    return content


def get_rss(url: str):
    rules = get_rules(url, "rss")
    html = Page(url).get()
    rss = Parser(rules, html).get_rss()
    return rss


def json2txt(content):
    data = ""
    for attr, value in content.items():
        data += f"{attr}:\n{value}\n\n"
    return data


def get_rules(url: str, data_type="rules"):
    u = urlparse(url)
    json_data = json.loads(files("nbweb").joinpath("data.json").read_text())
    for entry in json_data:
        e = urlparse(entry["url"])
        if u.hostname in e.hostname:
            return entry[data_type]
    raise TypeError("url not supported")
    return None
