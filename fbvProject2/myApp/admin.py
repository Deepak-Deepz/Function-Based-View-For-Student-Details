from django.contrib import admin
from myApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l =["sid","sname","sdob","smarks","sphone","saddr"]
admin.site.register(Student,StudentAdmin)
