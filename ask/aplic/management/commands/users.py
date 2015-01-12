#!/usr/bin/python
from datetime import datetime
from optparse import make_option
from django.core.management.base import BaseCommand

#from ask.models import Profile, Tag, Question, Answer
from django.contrib.auth.models import User

from faker.frandom import random
from faker.lorem import sentence, sentences, words
from mixer.fakers import get_username, get_email
from pprint import pformat

from django.db.models import Min, Max
import csv

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
		while(len(names.keys())<int(options['users'])):
		    names[get_username(length=30)]=1
		i = 1
		cout1=1
		count = 1
		p_min = 1
		p_max=10000
		c = csv.writer(open("users.csv", "wb"))
		p = csv.writer(open("profiles.csv", "wb"))
		q = csv.writer(open("questions.csv", "wb"))
		a = csv.writer(open("answers.csv", "wb"))
		t = csv.writer(open("tags.csv", "wb"))
		qt = csv.writer(open("qt.csv", "wb"))
		for name in names.keys():
			c.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, get_email(),random.randint(0,1),datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
			p.writerow([i, random.randint(0,20)])
			i=i+1
		for j in range(0, int(options['questions'])):
			numb_word = 3
			lis = words(numb_word)
			q.writerow([random.randint(p_min,p_max),(sentence())[0:59],sentences(3),datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
			for x in lis:
				t.writerow([x])
				qt.writerow([cout1,count])
				count = count+1
			cout1 = cout1+1
		for k in range(0, int(options['answers'])):
			a.writerow([sentences(3),datetime.now().strftime("%Y-%m-%d %H:%M:%S"),random.randint(0,1),random.randint(p_min,p_max),random.randint(p_min,100000)])
