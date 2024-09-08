from nbweb.utils import html2text


def convert_article_json_to_txt(article_json):
    article_txt = f"""{article_json.get("title")}\n{article_json.get("published_at")}\n{article_json.get("author")}\n{article_json.get("img")}\n\n\n{article_json.get("content")}"""
    return html2text(article_txt)


def convert_article_json_to_html(article_json):
    article_html = f"""<html><body><h1>{article_json.get("title")}</h1><p>{article_json.get("published_at")}</p><p>{article_json.get("author")}</p><img src="{article_json.get("img")}"><article>{article_json.get("content")}</article></body></html>"""
    return article_html
