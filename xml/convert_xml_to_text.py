import xml.etree.ElementTree as ET

def convert_to_desired_format(element, path=''):
    result = {}
    # Add the current element to the path
    path += '/' + element.tag
    # Process attributes of the current element
    if element.attrib:
        for attr_name, attr_value in element.attrib.items():
            attr_path = f"{path} (attribute_name)-{attr_name}"
            result[attr_path] = attr_value
    # Process text content of the element
    if element.text and element.text.strip():
        result[path] = element.text.strip()

    # Recursively process child elements
    for child in element:
        result.update(convert_to_desired_format(child, path))

    return result

xml_string = '''
<root>
<Waybill xmlns__colon__rsm="iata__colon__housewaybill__colon__1" xmlns__colon__ram="iata__colon__datamodel__colon__3" xmlns="iata__colon__waybill__colon__1">
</Waybill>
</root>
'''


def get_input_fields(xml_string):
    input_fields = []
    root = ET.fromstring(xml_string)
    result_dict = convert_to_desired_format(root, 'root')
    for key, value in result_dict.items():
        print(f"{key} = {value}")
        input_fields.append(key)

get_input_fields(xml_string)