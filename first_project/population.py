import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()


import random
from first_app.models import User

from faker import Faker

fake_data = Faker()



def data(N=5):

    for i in range(N):

        first_name  =fake_data.name()
        Last_name = fake_data.name()
        Email = fake_data.address()
        user = User.objects.get_or_create(name=first_name,last_name=Last_name,email=Email)


if __name__== '__main__':
    print('populating')
    data(20)
    print('complete')