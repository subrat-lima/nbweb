import xml.etree.ElementTree as ET
from datetime import datetime

from nbweb.extractor import get_valid_extractor


def get_content(url: str, return_type: str):
    extractor = get_valid_extractor(url)
    if extractor is None:
        raise TypeError("url not supported")
    content = extractor.extract(url)
    if return_type == "txt":
        return json2txt(content)
    return content


def check_is_supported(url: str) -> str:
    extractor = get_valid_extractor(url)
    if extractor is None:
        return "no"
    return "yes"


def json2txt(content):
    data = ""
    for attr, value in content.items():
        data += f"{value}\n\n"
    return data


def json2rss(rules, content):
    xml_string = """<?xml version="1.0" encoding="utf-8"?>
    <rss version="2.0">
        <channel>
            <title>Sample Feed</title>
            <description>For documentation &lt;em&gt;only&lt;/em&gt;</description>
            <link>http://example.org/</link>
            <pubDate>Sat, 07 Sep 2002 00:00:01 GMT</pubDate>
        </channel>
    </rss>
    """
    root = ET.fromstring(xml_string)
    channel = root.find("channel")
    title = channel.find("title")
    description = channel.find("description")
    link = channel.find("link")
    pubDate = channel.find("pubDate")
    title.text = rules["url"]
    description.text = rules["name"]
    link.text = rules["url"]
    pubDate = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    for article in content:
        item = ET.SubElement(channel, "item")
        title = ET.SubElement(item, "title")
        title.text = article["title"]
        link = ET.SubElement(item, "link")
        link.text = article["link"]
        description = ET.SubElement(item, "description")
        description.text = article["description"]
        pubDate = ET.SubElement(item, "pubDate")
        pubDate.text = article["published"]
        guid = ET.SubElement(item, "guid")
        guid.text = article["link"]

    xmlstr = ET.tostring(root, encoding="unicode")
    return xmlstr
