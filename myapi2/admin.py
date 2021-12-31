from django.contrib import admin
from .models import Employs

# Register your models here.

class AdminEmploys(admin.ModelAdmin):

    list_display = ['id','employid','name','position','branch']

admin.site.register(Employs, AdminEmploys)
