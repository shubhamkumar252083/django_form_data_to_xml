from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .generate_xml import dict_to_xml, get_xml_in_proper_format
from .xml_input_fields import *
from datetime import datetime

def home(request):
  return render(request, "home.html")

@csrf_exempt
def xml_form(request, xml_form_name):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S')
    if xml_form_name == "form_one":
        form_fields = {key: formatted_datetime if value == "formatted_datetime" else value for key, value in dict_one.items()}
        text_to_add = text_to_add_one
    elif xml_form_name == "form_two":
        form_fields =  {key: formatted_datetime if value == "formatted_datetime" else value for key, value in dict_two.items()}
        text_to_add = text_to_add_two
    elif xml_form_name == "form_three":
        form_fields =  {key: formatted_datetime if value == "formatted_datetime" else value for key, value in dict_three.items()}
        text_to_add = text_to_add_three

    if request.method == 'POST':
        d = {i:j for i, j in request.POST.items()}
        xml_data = dict_to_xml(d)
        formated_xml_data = get_xml_in_proper_format(xml_data, text_to_add)
        return render(request, 'output_xml.html', {"data_list":formated_xml_data})
        # return render(request, 'test.html', {"html_code":"<h1>hello</h1>"})
    else:
        return render(request, 'forms.html', {"form_fields":form_fields})
    

