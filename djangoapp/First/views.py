from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Style(request):
    return render(request, 'app.html')
    