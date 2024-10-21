# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import PlantsDetail

class PlantCRUD_CBVView(View):
    template_name = 'plant_crud.html'
    # Handle GET requests for reading data
    def get(self, request, *args, **kwargs):
        template_path = str(settings.BASE_DIR / 'templates' / 'plant_crud.html')
        if 'id' in kwargs:  # For single plant retrieval
            plant = get_object_or_404(PlantsDetail, pid=kwargs['id'])
            return render(request, template_path)
        else:  # For listing all plants
            plants = PlantsDetail.objects.all()
            return render(request, template_path)


    # Handle POST requests for creating or updating data
    def post(self, request, *args, **kwargs):
        if 'id' in kwargs:  # Updating an existing plant
            plant = get_object_or_404(PlantsDetail, pid=kwargs['id'])
            plant.pid = request.POST.get('id')
            plant.plant_name = request.POST.get('pname')
            plant.save()
            return redirect('plant-crud')
        else:  # Creating a new plant
            plant = PlantsDetail(pid=request.POST.get('id'),plant_name=request.POST.get('pname'))
            plant.save()
            return redirect('plant-crud')

    # Handle DELETE requests
    def delete(self, request, *args, **kwargs):
        print("State-previous")
        plant = get_object_or_404(PlantsDetail, pid=kwargs['id'])
        print("State-1")
        print(plant)
        plant.delete()
        return redirect('plant-crud')

