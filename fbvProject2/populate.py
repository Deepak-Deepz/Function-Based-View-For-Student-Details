import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbvProject2.settings')
django.setup()
from faker import Faker
from myApp.models import Student
f = Faker()
def populate(n):
    for i in range(n):
        fsid = f.random_int(min =1, max =20)
        fsname = f.name()
        fsdob = f.date_of_birth()
        fsmarks = f.random_int(min = 1, max =100)
        fsphone = f.random_int(min = 1000, max =100000)
        fsaddr = f.address()
        s = Student.objects.get_or_create(sid = fsid, sname = fsname, sdob = fsdob,smarks =fsmarks,sphone = fsphone,saddr = fsaddr)

populate(20)
