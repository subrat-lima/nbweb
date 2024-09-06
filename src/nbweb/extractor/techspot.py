from .common import InfoExtractor


class TechSpotIE(InfoExtractor):
    _IE_NAME = "techspot"
    _VALID_URLS = [r"https://www.techspot.com/news/(?P<id>[\w-]+)"]
    _TESTS = []

    def _extract(self, url):
        id = self.get_id(url)
        webpage = self._request_webpage(url)
        title = self._query_selector(webpage, "h1::text")
        content = self._query_selector(
            webpage,
            "div.articleBody > :not(div.subDriveRevBot):not(.twitter-tweet):not(div.related-news):not(style) *::text",
        )

        return {"id": id, "title": title, "content": content}
