import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','school.settings')

import django
django.setup()

import random
from basic_app.models import student_table, teacher_table
from faker import Faker
import random

fakegen = Faker()

branch = ['CSE', 'IT', 'Civil', 'Mechinal', 'Electronics']
salary_tea = [50000, 60000, 55000, 70000, 65000, 80000]

def populate(N=10):
    for entry in range(N):

        fake_name = fakegen.name()
        fake_name2 = fakegen.name()

        fake_address = fakegen.address()
        fake_address2 = fakegen.address()

        studentro = student_table.objects.get_or_create(first_name=fake_name.split()[0], last_name=fake_name.split()[1], address=fake_address, student_branch=random.choice(branch))

        teachero = teacher_table.objects.get_or_create(first_name=fake_name2.split()[0], last_name=fake_name2.split()[1], address=fake_address2, salary=random.choice(salary_tea))

if __name__ == '__main__':
    print('Populating Script')
    populate(20)
    print('Pupulation Done')