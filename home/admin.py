from django.contrib import admin
from .models import Profile, Shopping_Cart, Build, CPU, Motherboard

class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'motherboard_manufacturer', 'cpu_socket_type')
    search_fields = ('name',)
    list_filter = ('motherboard_manufacturer', 'cpu_socket_type')

class CPUAdmin(admin.ModelAdmin):
    list_display = ('cpu_manufacturer', 'cpu_name', 'socket_type')
    search_fields = ('cpu_name',)
    list_filter = ('cpu_manufacturer', 'socket_type')

    
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(CPU, CPUAdmin)

admin.site.register(Profile)
admin.site.register(Shopping_Cart)
admin.site.register(Build)
