from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Category)

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'users', 'available', 'star', 'promo', 'created_at')

admin.site.register(Articles, ArticleAdmin)
admin.site.register(Images)