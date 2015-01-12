#!/usr/bin/python
from datetime import datetime
from optparse import make_option
from django.core.management.base import BaseCommand

from aplic.models import Profile, Tag, Question, Answer
from django.contrib.auth.models import User

from faker.frandom import random
from faker.lorem import sentence, sentences, words
from mixer.fakers import get_username, get_email
from pprint import pformat

from django.db.models import Min, Max

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--users',
            action='store',
            dest='users',
            default=0,
        ),
        make_option('--questions',
            action='store',
            dest='questions',
            default=0,
        ),
        make_option('--answers',
            action='store',
            dest='answers',
            default=0,
        ),
    ) 


    def handle(self, *args, **options):
        names = {}
        while (len(names.keys())<int(options['users'])):
            names[get_username(length=30)]=1

        for name in names.keys():
            u = User.objects.create(username=name, email=get_email())
            p = Profile.objects.create(user_id=u.id, rating=random.randint(0,20))


        p_min = Profile.objects.all().aggregate(Min('id'))['id_min']
        p_max = Profile.objects.all().aggregate(Max('id'))['id_max']


        for i in range(0, int(options['questions'])):
            q=Question.objects.create(author_id=random.randint(p_min,p_max),
                title=(sentence())[0:59], text = sentences(3))

        for j in lis:
            t = Tag.objects.create(word = j)

        for i in range(0, int(options['answers'])):
            a = Answer.objects.create(text = (sentence())[0:59], author_id = random.randint(p_min,p_max),)