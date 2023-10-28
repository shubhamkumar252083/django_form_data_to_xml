import xml.etree.ElementTree as ET
import xml.dom.minidom


def dict_to_xml(d):
    root = ET.Element("root")
    for key, value in d.items():
        elements = key.split('/')
        current = root
        previous_element = 0
        for element in elements:
            if "(attribute_name)" in element:
                # continue
                pair = element.split(" (attribute_name)-")
                attr_name = pair[1]
                element = pair[0]
                if element not in [child.tag for child in current]:
                    child = ET.SubElement(current, element)
                    child.set(attr_name, value)
                elif element in [child.tag for child in current]:
                    child.set(attr_name, value)
                current = [child for child in current if child.tag == element][0]
            else:
                if element not in [child.tag for child in current]:
                    child = ET.SubElement(current, element)
                current = [child for child in current if child.tag == element][0]
        if value and "(attribute_name)" not in key:
            current.text = value
    return ET.tostring(root).decode()
    # # print(f'ET.tostring(root).decode() ==> {ET.tostring(root).decode()}')
    # formatted_xml = ET.tostring(root, encoding='unicode', method='xml')
    # dom = xml.dom.minidom.parseString(formatted_xml)
    # # Pretty-print the XML
    # formatted_xml = dom.toprettyxml()
    # print(f'formatted_xml ==> {formatted_xml}')
    # return formatted_xml


def get_xml_in_proper_format(xml_text, text_to_add):
    data = []
    data.extend(text_to_add["first"])
    xml_text = xml_text.replace(":", "__colon__").replace("<root><root>" , "").replace("</root></root>", "")
    dom = xml.dom.minidom.parseString(xml_text)
    formatted_xml = dom.toprettyxml()
    # Remove the XML declaration
    formatted_xml = formatted_xml.replace('<?xml version="1.0" ?>\n', '')
    # print(formatted_xml) # properly formated xml with proper indentation.
    for i in formatted_xml.split("\n"):
        if "__colon__" in i or "__duplicate__" in i:
            data.append(i.replace("__colon__", ":").replace("__duplicate__", ""))
        elif i in ("<root>", "</root>", "<check>", "</check>"):
            continue
        elif "<check>" in i or "</check>" in i:
            continue 
        else:
            data.append(i)
    data.extend(text_to_add["last"])
    return data
