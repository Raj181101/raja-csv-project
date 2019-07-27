from django.contrib import admin
from csvapp.models import Login,File
# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display=['files']

admin.site.register(Login)
admin.site.register(File,FileAdmin)