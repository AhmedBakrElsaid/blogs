from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin (admin.ModelAdmin):
    list_display = ['title','active']
    search_fields = ['title']
    list_filter = ['active']
    

admin.site.register(Post,PostAdmin)