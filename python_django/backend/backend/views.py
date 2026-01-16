from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello Django World")
    return render(request = request, template_name='index.html')

def about(request):
    return HttpResponse("Hello this is about page ")

def contact(request):
    return HttpResponse("Hello this is contact page")
