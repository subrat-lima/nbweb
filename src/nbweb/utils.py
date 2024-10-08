import re


def strip_html_attrs(html):
    html = re.sub(
        r"<\s*(?P<tag>\w+)[^>]*?>", lambda pattern: f'<{pattern.group("tag")}>', html
    )
    return html


def html2text(html):
    html = re.sub(r"<br/?>", "\n\n", html)
    html = re.sub(r"<\s*/\s*(p|div|section|article)\s*>", "\n\n", html)
    html = re.sub(r"<\s*/?[\w-]+[^>]*?>", "", html)
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"[\n]{3,}", "\n\n\n", html)
    html = html.strip()
    return html
