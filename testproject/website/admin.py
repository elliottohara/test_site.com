from django.contrib import admin

# Register your models here.
from website.models import Staff, Class

admin.site.register(Staff)
admin.site.register(Class)