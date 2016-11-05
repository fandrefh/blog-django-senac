from django.contrib import admin

from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    exclude = ('autor',)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
