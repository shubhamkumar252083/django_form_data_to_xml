import xml.etree.ElementTree as ET

# Sample XML data with empty tags
xml_data = '''
<root>
    <root>
        <version>1.0</version>
        <element1>value1</element1>
        <element2>value2</element2>
        <element3 check="10">
            < />
            <subelement1>subvalue1</subelement1>
            <subelement2>subvalue2</subelement2>
        </element3>
    </root>
</root>
'''

def preprocess_xml(xml_str):
    # Remove empty tags
    cleaned_xml = xml_str.replace('< />', '')
    return cleaned_xml

def remove_empty_tags(element):
    for child in list(element):
        remove_empty_tags(child)
    for elem in element.findall('.//'):
        if not elem.text and not elem.tail and len(elem) == 0:
            elem.getparent().remove(elem)

def main_clean_xml(xml_str):
    # Preprocess the XML
    cleaned_xml_data = preprocess_xml(xml_data)
    # Parse the cleaned XML
    root = ET.fromstring(cleaned_xml_data)
    # Remove empty tags starting from the root
    remove_empty_tags(root)
    # Convert the modified tree back to XML
    cleaned_xml = ET.tostring(root, encoding='utf8').decode('utf8')
    # print(cleaned_xml)
    return cleaned_xml

# print(main_clean_xml(xml_data))