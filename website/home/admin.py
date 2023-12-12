from django.contrib import admin

from django.contrib import admin
from .models import PostModel
from .models import SliderModel


# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_post')

admin.site.register(PostModel, PostModelAdmin)

class SliderModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_img')

admin.site.register(SliderModel, SliderModelAdmin)
