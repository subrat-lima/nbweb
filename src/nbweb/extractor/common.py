import re

from parsel import Selector

from nbweb.page import Page


class InfoExtractor:
    @classmethod
    def _is_valid_url(cls, url):
        for _REGEX in cls._VALID_URLS:
            match = re.search(_REGEX, url)
            if match is not None:
                return True
        return False

    def _request_webpage(self, url):
        page = Page(url)
        return page.get()

    def _get_id(self, url):
        for _REGEX in self._VALID_URLS:
            match = re.search(_REGEX, url)
            if match is None:
                continue
            return match.group("id")
        return url

    def _get_html_title(self, webpage):
        parser = Selector(text=webpage)
        title = parser.css("title::text").get()
        return title

    def _query_selector(self, webpage, selector):
        parser = Selector(text=webpage)
        content = parser.css(selector).getall()
        if content is not None:
            return "\n".join(content)

    def extract(self, url):
        return self._extract(url)
