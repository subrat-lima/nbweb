from nbweb.page import Page
from nbweb.parser import Parser

from urllib.parse import urlparse


def get_content(url):
    html = Page(url).get()
    o = urlparse(url)
    domain = f"{o.scheme}://{o.netloc}"
    content = Parser(url, html).get()
    return content
