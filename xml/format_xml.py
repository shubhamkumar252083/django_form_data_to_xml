import xml.dom.minidom
# Parse the XML content
xml_string = """<root>
    <element1>value1</element1>
    <element2>value2</element2>
</root>"""

dom = xml.dom.minidom.parseString(xml_string)

# Pretty-print the XML
formatted_xml = dom.toprettyxml()

print(formatted_xml)