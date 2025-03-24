from django.contrib import admin
from posts.models import Post

# Register your models here.

@admin.register(Post)
class ModelNameAdmin(admin.ModelAdmin):
    #pass indica que la clase está vacía.
    list_display = ['title','create_at']

