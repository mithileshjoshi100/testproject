from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')

def project_list(request):
    return render(request, 'homepage/projectlist.html')
