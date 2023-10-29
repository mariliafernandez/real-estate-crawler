import re

def get_element_text(element):
    if element:
        return element.text
    return None


def get_elements_attr(elements, attr):
    return [el[attr] for el in elements]


def get_element_attr(element, attr):
    if element:
        return element[attr]
    return None
