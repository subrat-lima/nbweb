from .common import InfoExtractor


class TechSpotIE(InfoExtractor):
    _IE_NAME = "techspot"
    _VALID_URLS = [r"https://www.techspot.com/news/(?P<id>[\d]+)[\w-]+"]
    _TESTS = [{
            "url": "https://www.techspot.com/news/104596-lenovo-auto-twist-pc-has-display-automatically-follows.html",
            "info_dict": {
                "id": "104596",
                "title": "Lenovo's crazy \"Auto Twist\" PC can turn and face you automatically",
            },
        }]

    def _extract(self, url):
        id = self._get_id(url)
        webpage = self._request_webpage(url)
        title = self._get_meta_property(webpage, "title")
        content = self._query_selector(
            webpage,
            "div.articleBody > :not(div.subDriveRevBot):not(.twitter-tweet):not(div.related-news):not(style) *::text",
        )

        return {"id": id, "title": title, "content": content}
