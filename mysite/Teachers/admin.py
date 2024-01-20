from django.contrib import admin

from .models import TeachersInfo, ContractType

# Register your models here.

admin.site.register(TeachersInfo)
admin.site.register(ContractType)