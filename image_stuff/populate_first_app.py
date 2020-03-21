import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_stuff.settings')

import django
django.setup()

import random
from testing.models import AccesssRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):
    
    for entry in range(N):
        
        # Get Topic For Entry
        top = add_topic()

        # Create Fake Data For Entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # New Webpage Entry
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        # Create fake access record
        acc_rec = AccesssRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print('Populating Script')
    populate(10)
    print('Populating Complete')