import pytest

from nbweb.utils import html2text, strip_html_attrs

_TEST_SAMPLE_FOR_HTML2TEXT_FUNCTION = [
    ("no-html", "hello world", "hello world"),
    ("simple-html", "<html>hello world</html>", "hello world"),
    (
        "strip-extra-spaces",
        " <html>   <body>  <div>  hello   world   </div>   </body>   </html>  ",
        "hello world",
    ),
    ("simple-paragraph", "<p>hello</p><p>world</p>", "hello\nworld"),
    ("simple-br-tag-1-non-self-closing", "hello<br>world", "hello\nworld"),
    ("simple-br-tag-2-self-closing", "hello<br/>world", "hello\nworld"),
]


@pytest.mark.parametrize(
    "description,input,expected", _TEST_SAMPLE_FOR_HTML2TEXT_FUNCTION
)
def test_html2text(description, input, expected):
    output = html2text(input)
    assert output == expected


_TEST_SAMPLE_FOR_STRIP_HTML_ATTRS_FUNCTION = [
    ("no-html", "hello world", "hello world"),
    ("simple-html", "<html>hello world</html>", "<html>hello world</html>"),
    ("simple-attrs", '<p id="content">hello world</p>', "<p>hello world</p>"),
    ("simple-br-tag-1-non-self-closing", "hello<br>world", "hello<br>world"),
    ("simple-br-tag-2-self-closing", "hello<br/>world", "hello<br>world"),
]


@pytest.mark.parametrize(
    "description,input,expected", _TEST_SAMPLE_FOR_STRIP_HTML_ATTRS_FUNCTION
)
def test_strip_html_attrs(description, input, expected):
    output = strip_html_attrs(input)
    assert output == expected
