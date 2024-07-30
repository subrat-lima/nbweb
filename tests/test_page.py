from nbweb.page import Page

import pytest


def test_failure():
    url = "https://subratlima.xyz"
    p = Page(url)
    html = p.get()
    assert html is None


def test_success():
    url = "https://httpbin.org"
    p = Page(url)
    html = p.get()
    assert html is not None


def monkeypatch_func(*args, **kwargs):
    return "one two three"


def test_load_from_cache(monkeypatch):
    url = "https://httpbin.org/get"
    p = Page(url)
    html = p.get()
    assert html is not None
    assert html != "one two three"

    monkeypatch.setattr(Page, "_fetch_from_cache", monkeypatch_func)
    p2 = Page(url)
    html = p2.get()

    assert html == "one two three"
