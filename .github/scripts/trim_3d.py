"""Strip the language pie chart and the contributions/stars/forks line
from the 3D contribution graph, keeping the 3D calendar and radar chart."""
import sys
import xml.etree.ElementTree as ET

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)

path = sys.argv[1]
tree = ET.parse(path)
root = tree.getroot()

for child in list(root):
    if child.tag != f"{{{NS}}}g":
        continue
    text = " ".join(t.text or "" for t in child.iter() if t.text)
    is_pie = child.attrib.get("transform", "").startswith("translate(40,")
    is_stats_line = "transform" not in child.attrib and "contributions" in text
    if is_pie or is_stats_line:
        root.remove(child)

tree.write(path, encoding="unicode")
