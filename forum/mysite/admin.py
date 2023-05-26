from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(Types)
admin.site.register(Person)
admin.site.register(Organisation)

@admin.register(Request)
class Request(admin.ModelAdmin):
    list_display = ['first_name', 'type', 'datetime', 'text']
    list_filter = ['type', 'datetime']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['category', 'datetime', 'text']
    list_filter = ['category']




