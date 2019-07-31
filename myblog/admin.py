from django.contrib import admin
from myblog.models import Post, Genre

class GenreInline(admin.TabularInline):
    model = Genre.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        GenreInline,
    ]
    
class GenreAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)

admin.site.register(Genre, GenreAdmin)