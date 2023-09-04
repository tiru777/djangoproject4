from django.contrib import admin
from app.models import Employee


# Register your models here.


class MyEmployee(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')


admin.site.register(Employee, MyEmployee)
