from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .generate_xml import dict_to_xml
from .xml_input_fields import texts_one

def home(request):
  return render(request, "test.html")


@csrf_exempt
def xml_form(request):
    if request.method == 'POST':
        d = {i:j for i, j in request.POST.items()}
        xml_data = dict_to_xml(d)
        return render(request, 'output_xml.html', {"html_code":xml_data})
    else:
        return render(request, 'forms.html', {"texts":texts_one})
    
