from django.contrib import admin
from .models import Post, Comment



class CommentInline(admin.TabularInline):
    model = Comment



class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
    list_display = ('title', 'author', 'created_at',)


admin.site.register(Post, BlogAdmin)
admin.site.register(Comment)

# Register your models here.
