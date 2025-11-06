from django.http import HttpResponse
from django.shortcuts import render


def index(request):
     return render(resquest, 'demo_site.html')
# Create your views here.
