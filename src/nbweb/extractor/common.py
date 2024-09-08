import re

from parsel import Selector

from nbweb.page import Page


class InfoExtractor:
    _VALID_URLS: list[str] = []

    @classmethod
    def _is_valid_url(cls, url: str) -> bool:
        for _REGEX in cls._VALID_URLS:
            match = re.search(_REGEX, url)
            if match is not None:
                return True
        return False

    def _request_webpage(self, url: str) -> str | None:
        page = Page(url)
        return page.get()

    def _get_id(self, url: str) -> str | None:
        for _REGEX in self._VALID_URLS:
            match = re.search(_REGEX, url)
            if match is None:
                continue
            return match.group("id")
        return url

    def _get_meta_property(self, webpage: str, property: str) -> str | None:
        parser = Selector(text=webpage)
        content = parser.css(f"meta[name='{property}']::attr(content)").get()
        if content is None:
            content = parser.css(f"meta[property='{property}']::attr(content)").get()
        return content

    def _get_html_title(self, webpage: str) -> str | None:
        parser = Selector(text=webpage)
        title = parser.css("title::text").get()
        return title

    def _query_selector(self, webpage: str, selector: str) -> str | None:
        parser = Selector(text=webpage)
        content = parser.css(selector).get()
        return content

    def _query_jmespath(self, webpage: str, selector: str) -> str | None:
        parser = Selector(text=webpage)
        elems = parser.jmespath(selector).getall()
        if elems is not None and len(elems) > 0:
            return "\n".join(elems)
        return ""

    def _query_selector_all(self, webpage: str, selector: str) -> list[str]:
        parser = Selector(text=webpage)
        content = parser.css(selector).getall()
        return content

    def extract(self, url: str) -> dict[str, str]:
        return self._extract(url)

    def _extract(self, url: str) -> dict[str, str]:
        return {}
