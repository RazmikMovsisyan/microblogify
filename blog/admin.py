from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
