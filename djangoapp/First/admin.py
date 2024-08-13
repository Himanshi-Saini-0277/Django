from django.contrib import admin

# Register your models here.
from .models import Employee, Book

admin.site.register(Employee)
admin.site.register(Book)

admin.site.site_header = "Himanshi's Blog App"
admin.site.site_title = "First Blog App"
admin.site.index_title = "Blog Application"
