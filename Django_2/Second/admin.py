from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)

admin.site.site_header = "Himanshi's Blog App"
admin.site.site_title = "First Blog App"
admin.site.index_title = "Blog Application"
