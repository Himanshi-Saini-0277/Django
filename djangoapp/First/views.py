from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Employee, Book

def app(request):
    emp = Employee.objects.all()
    books = Book.objects.all()
    return render(request, 'app.html', {'emp': emp, 'books': books})
    
def Style(request):
    return render(request, 'Style.css')
