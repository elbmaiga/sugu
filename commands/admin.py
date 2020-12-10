from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Container)
admin.site.register(Panner_Articles)
admin.site.register(Panner)

# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('email', 'telephone', 'address')
# admin.site.register(Client, ClientAdmin)

# class CommandAdmin(admin.ModelAdmin):
#     list_display = ('client', 'status', 'deliverance', 'created_at')
# admin.site.register(Commands, CommandAdmin)
# admin.site.register(Articles_On_Panner)