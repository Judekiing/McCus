from django.contrib import admin
from .models import Post



class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'updated_at', 'created_at',)

admin.site.register(Post, BlogAdmin)

# Register your models here.
