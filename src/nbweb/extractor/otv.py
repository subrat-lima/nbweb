from .common import InfoExtractor


class OTVIE(InfoExtractor):
    _IE_NAME = "otv"
    _VALID_URLS = [
        r"https://odishatv.in/news/(?:\w+)/(?P<id>[\w-]+)",
        r"https://otvkhabar.in/news/(?:\w+)/[\w-]+/(?P<id>[\d]+)",
    ]
    _TESTS = [
        {
            "url": "https://odishatv.in/news/weather/cyclonic-circulation-over-north-coastal-andhra-pradesh-low-pressure-bay-of-bengal-on-september-5-243347",
            "info_dict": {
                "id": "cyclonic-circulation-over-north-coastal-andhra-pradesh-low-pressure-bay-of-bengal-on-september-5-243347",
                "title": "Cyclonic circulation over north Coastal Andhra Pradesh; low-pressure over Bay of Bengal around September 5",
                "description": "md5:776d4bb900a435219f02deff65bfae9c",
                "published_at": "Wednesday, 04 September 2024",
                "img": "https://images.odishatv.in/uploadimage/library/16_9/16_9_5/recent_photo_1721217447.jpg",
            },
        },
        {
            "url": "https://odishatv.in/news/festivals-events/cuttack-bali-jatra-to-kick-off-from-november-15-243389",
            "info_dict": {
                "id": "https://odishatv.in/news/festivals-events/cuttack-bali-jatra-to-kick-off-from-november-15-243389",
                "title": "Cuttack Bali Jatra to kick off from November 15",
                "description": "md5:12502136d1a7a40d2b0b80f647a84681",
                "published_at": "Thursday, 05 September 2024",
                "img": "https://images.odishatv.in/uploadimage/library/16_9/16_9_5/recent_photo_1701422955.jpg",
            },
        },
        {
            "url": "https://otvkhabar.in/news/human-interest/teachers-day-inspiring-teachers-lead-the-path-of-success-for-students-by-taking-bold-steps/135675",
            "info_dict": {
                "id": "https://otvkhabar.in/news/human-interest/teachers-day-inspiring-teachers-lead-the-path-of-success-for-students-by-taking-bold-steps/135675",
                "title": "ଏଭଳି ମହାନ୍ ଗୁରୁଙ୍କୁ ଶତ ନମନ; ଶିକ୍ଷାର ବିକାଶ ପାଇଁ ନେଇଛନ୍ତି ବଳିଷ୍ଠ ପଦକ୍ଷେପ...",
                "description": "md5:fd7ddc94fe40947e1149533b98d96b70",
                "published_at": "Thursday, 05 September 2024",
                "img": "https://images.odishatv.in/uploadimage/library/16_9/16_9_0/IMAGE_1725510830.jpg",
            },
        },
    ]

    def _extract(self, url):
        id = self._get_id(url)
        webpage = self._request_webpage(url)
        title = self._query_selector(webpage, "h1::text")
        description = self._query_selector(
            webpage, "div.article-content > p::text"
        ).strip()
        published_at = self._query_selector(
            webpage, "ul.article-author:nth-child(3) > li:nth-child(1)::text"
        ).replace("Published: ", "")
        img = self._get_meta_property(
            webpage,
            "og:image",
        )
        # author = self._get_meta_property(webpage, "author")
        content = self._query_selector(webpage, "div.article-content > p::text").strip()

        return {
            "id": id,
            "title": title,
            "description": description,
            "published_at": published_at,
            "img": img,
            "content": content,
        }


class OTVListIE(InfoExtractor):
    _IE_NAME = "otv"
    _VALID_URLS = [
        r"https://odishatv.in/(?P<id>\w+)",
        # r"https://otvkhabar.in/news/(?:\w+)/[\w-]+/(?P<id>[\d]+)",
    ]
    _TESTS = []
    _TESTSS = [
        {
            "url": "https://odishatv.in/sports",
            "info_dict": {
                "id": "sports",
                "min_count": 15,
            },
        },
    ]

    def _extract(self, url):
        # id = self._get_id(url)
        webpage = self._request_webpage(url)

        news_articles = []

        articles = self._query_selector_all(
            webpage,
            "div.listing-news-start .listing-result-news, div.mobile-listing-start div.mobile-listing",
        )
        for article in articles:
            news_articles.append(
                {
                    "title": self._query_selector(article, "h5::text"),
                    "link": self._query_selector_all(
                        article, "a:nth-child(1)::attr(href)"
                    )[0],
                    "description": self._query_selector(article, "p::text"),
                    "published": self._query_selector(
                        article, "ul > li:first-child::text"
                    ),
                }
            )

        return news_articles
