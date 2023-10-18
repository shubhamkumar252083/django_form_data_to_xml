import xml.etree.ElementTree as ET

def xml_to_dict(element, path=""):
    result = {}
    count = 1
    for child in element:
        child_path = f"{path}/{child.tag}"
        if child.attrib:
            for attr_name, attr_value in child.attrib.items():
                attr_path = f"{count}__{child_path} (attribute_name)-{attr_name}"
                result[attr_path] = attr_value
                count +=1
        if list(child):
            child_path = f'{count}__{child_path}'
            result.update(xml_to_dict(child, path=child_path))
            count += 1
        else:
            child_path = f'{count}__{child_path}'
            result[child_path] = child.text
            count +=1

    return result

xml_data = """
<root>
<Waybill xmlns__colon__rsm="iata__colon__housewaybill__colon__1" xmlns__colon__ram="iata__colon__datamodel__colon__3" xmlns="iata__colon__waybill__colon__1">
</Waybill>
</root>
"""


root = ET.fromstring(xml_data)
result_dict = xml_to_dict(root, "root")

count = 1
for key, value in result_dict.items():
    parts = key.split("__")
    print(f"{count}_{parts[-1]} = {value}")
    count += 1

