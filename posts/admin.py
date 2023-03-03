from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin): 
    list_display = ["__str__", "data"]
    list_filter = ["data"]
    search_fields = ["titolo", "contenuto"]
    prepopulated_fields = {"slug": ("titolo",) }

    class Meta:
        model = Post



# Register your models here.
admin.site.register(Post, PostAdmin)