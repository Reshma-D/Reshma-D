import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
xmls_file = os.listdir("data/1415/annotations/xmls")

for xmls in xmls_file:
    PATH = "data/1415/annotations/xmls/" + xmls
    with open(PATH, encoding='latin-1') as f:
        tree = ET.parse(f)
        root = tree.getroot()

    for elem in root.getiterator():
        try:
            # elem.text = elem.text.replace("../../data/1415/image/","data/1415/image/")
            elem.text = elem.text.replace("/image/","/images/")
        except AttributeError:
            pass
    tree.write(PATH)