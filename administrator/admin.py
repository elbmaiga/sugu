from django.contrib import admin

from .models import *
# Register your models here.
class PanelCategory(admin.ModelAdmin):
    list_display = ('category', 'description')
admin.site.register(Category)

class PanelAdmin(admin.ModelAdmin):
    list_display = ('username', 'activity_name', 'category')
admin.site.register(Administrator, PanelAdmin)
