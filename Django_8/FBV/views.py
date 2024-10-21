from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PlantsForm  
from .models import Plants  

def plantV(request):  
    if request.method == "POST":  
        form = PlantsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = PlantsForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    plants = Plants.objects.all()  
    return render(request,"show.html",{'plants':plants})  

def edit(request, id):  
    plant = get_object_or_404(Plants, id=id)  
    return render(request,'edit.html', {'plant':plant})  

def update(request, id):  
    plant = get_object_or_404(id=id)  
    form = PlantsForm(request.POST, instance = plant)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'plant': plant})  

def destroy(request, id):  
    plant = Plants.objects.get(id=id)  
    plant.delete()  
    return redirect("/show")  


