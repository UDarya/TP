#!/usr/bin/python

from optparse import make_option
from django.core.management.base import BaseCommand

#from ask.models import Profile, Tag, Question, Answer
#from django.contrib.auth.models import User

from faker.frandom import random
from faker.lorem import sentence, sentences
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
	)

	def handle(self, *args, **options):
		names = {}
		while(len(names.keys())<int(options['users'])):
		    names[get_username(length=30)]=1
		#if options['users']
		c = csv.writer(open("users.csv", "wb"))
		#p = csv.writer(open("profiles.csv", "wb"))
		for name in names.keys():
			c.writerow([name, get_email()])
			#p.writerow([u.id, random.randint(0,20)])


