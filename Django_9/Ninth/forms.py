from django import forms  
from .models import AppUsers
class UserForm(forms.ModelForm):  
    class Meta:  
        model = AppUsers 
        fields = "__all__"  