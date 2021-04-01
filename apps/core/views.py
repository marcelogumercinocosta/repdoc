from apps.core.models import Documento
from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
class DocumentosListView( ListView, ):
    template_name = 'core/documento_list.html'
    model = Documento