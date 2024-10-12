from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'tags')
    list_filter = ('tags',)

admin.site.site_header = "Himanshi's Blog App"
admin.site.site_title = "First Blog App"
admin.site.index_title = "Blog Application"
