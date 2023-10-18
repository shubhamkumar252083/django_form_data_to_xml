from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .generate_xml import dict_to_xml
from .xml_input_fields import *

def home(request):
  return render(request, "home.html")

@csrf_exempt
def xml_form(request, xml_form_name):
    if xml_form_name == "form_one":
        form_fields = dict_one
    elif xml_form_name == "form_two":
        form_fields = dict_two
    elif xml_form_name == "form_three":
        form_fields = dict_three

    if request.method == 'POST':
        d = {i:j for i, j in request.POST.items()}
        xml_data = dict_to_xml(d)
        return render(request, 'output_xml.html', {"html_code":xml_data})
    else:
        return render(request, 'forms.html', {"form_fields":form_fields})
    
