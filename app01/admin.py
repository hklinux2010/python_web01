from django.contrib import admin
from app01.models import Test2,Contact,Tag


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    fields = ('name','email')

admin.site.register([Test2,Contact,Tag])




