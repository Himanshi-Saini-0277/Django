"""
URL configuration for Django_8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FBV import views  
from Eight.views import PlantCRUD_CBVView

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('plant', views.plantV),  
    path('show',views.show),  
    path('edit/<int:id>/', views.edit, name='edit'),  
    path('update/<int:id>/', views.update, name='update'),  
    path('delete/<int:id>/', views.destroy),
    path('plants/', PlantCRUD_CBVView.as_view(), name='plant-crud'),  # For listing and creating
    path('plants/<int:id>/', PlantCRUD_CBVView.as_view(), name='plant-crud'), 
]
