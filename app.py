import sys
import codecs
import re
import difflib
from lxml import html, etree
from html_item import HtmlItem


def main():
    original_html_path = str(sys.argv[1])
    modified_html_path = str(sys.argv[2])
    element_id = str(sys.argv[3])

    original_html = open_html(original_html_path)
    modified_html = open_html(modified_html_path)

    original_element = find_element_by_id(original_html, element_id)
    if original_element != None:
        print("Original Element:")
        original_element.tostring()
        element_type = get_element_type(original_element.html_code)
        properties = get_properties(original_element.html_code)
        if len(properties) > 0:
            closest_item = find_element_by_properties(modified_html, properties, element_type, original_element)
            if closest_item != None:
                print("Closest Element:")
                closest_item.tostring()
            else:
                print("No close element found")
        else:
            print("The item doesn't have enough properties to find it in another html")
    else:
        print("Html element with id: {} not found".format(element_id))
    sys.exit(0)


def open_html(html_path):
    return codecs.open(html_path,'r').read()


def find_element_by_id(html_page, id):
    root = etree.fromstring(html_page)
    tree = root.getroottree()
    xpath_by_id = '//*[@id="' + id + '"]'
    result = root.xpath(xpath_by_id)
    if len(result) > 0:
        element = result[0]
        return HtmlItem(etree.tostring(element), tree.getpath(element))
    else:
        return None


def get_element_type(html_code):
    element_type_regex = r"\<\/\w*\>"
    return re.search(element_type_regex, html_code, re.IGNORECASE).group(0).replace("/", "").replace("<", "").replace(">", "")


def get_properties(element):
    properties_regex = r"\w*\=\"[\w\-\#\s\:\(\)\;\.]*\""
    if re.search(properties_regex, element, re.IGNORECASE):
        return re.findall(properties_regex, element, re.IGNORECASE)


def find_element_by_properties(html_page, properties, element_type, original_element):
    root = etree.fromstring(html_page)
    properties_matches = {}
    html_items = []
    match_candidates = []
    for prop in properties:
        find_element_by_property(prop, element_type, root, properties_matches, html_items)
    for key in properties_matches:
        for item in (properties_matches[key]):
            match_candidates.append(item.html_code)
    return get_closest_match(original_element, match_candidates, html_items)


def find_element_by_property(prop, element_type, root, properties_matches, html_items):
    tree = root.getroottree()
    xpath_by_attr = '//' + element_type + '[@' + prop + ']'
    elements = root.xpath(xpath_by_attr)
    for elem in elements:
        html_items.append(HtmlItem(etree.tostring(elem), tree.getpath(elem)))
    properties_matches[prop] = html_items


def get_closest_match(original_element, match_candidates, html_items):
    match = difflib.get_close_matches(original_element.html_code, match_candidates, 1)
    if len(match) > 0:
        html_items = list(filter(lambda x: x.html_code == match[0], html_items))
        if len(html_items) > 0:
            return html_items[0]
        else:
            return None
    else:
        return None


main()