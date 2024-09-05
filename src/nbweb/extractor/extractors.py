from ._extractors import *  # noqa: F403


def get_all_extractors():
    extractors = []
    for name, klass in globals().items():
        if name.endswith("IE"):
            extractors.append(klass)
    return extractors


def get_extractor_by_name(name):
    for extractor_name, klass in globals().items():
        if extractor_name == name:
            return klass()
    return None


def get_valid_extractor(url):
    _ALL_EXTRACTORS = get_all_extractors()
    for extractor in _ALL_EXTRACTORS:
        klass = extractor()
        if klass._is_valid_url(url):
            return klass
    return None
