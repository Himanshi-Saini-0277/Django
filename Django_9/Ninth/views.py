from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from .forms import UserForm  
from .models import AppUsers 

def sendEmail(request):
    result=""
    e_address = AppUsers.objects.all()
    if request.method == 'POST':
        
        address = request.POST.get('e_address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if address and subject and message:
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [address],  # Sending to the selected email address
                )
                result = 'Email sent successfully'
            except Exception as e:
                result = f'Error sending email: {str(e)}'
        else:
            result = 'All fields are required'

    return render(request, "email.html", {'result': result, 'e_address': e_address})


def userV(request):  
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = UserForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    users = AppUsers.objects.all()  
    return render(request,"show.html",{'users':users})  

def edit(request, id):  
    user = AppUsers.objects.get(user_id=id)  
    return render(request,'edit.html', {'user':user})  

def update(request, id):  
    user = AppUsers.objects.get(user_id=id)  
    form = UserForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'user': user})  

def destroy(request, id):  
    user = AppUsers.objects.get(user_id=id)  
    user.delete()  
    return redirect("/show")  


