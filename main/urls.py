
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name ="home"),
    path('xml_form/<str:xml_form_name>/', xml_form, name='xml_form'),
    path('admin/', admin.site.urls),
]
