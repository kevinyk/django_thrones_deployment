from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PersonManager(models.Manager):
	def validate_person(self, post_data):
		# THIS IS WHERE VALIDATION HAPPENS
		# we need to hold on to all of our error messages
		error_msgs = []
		houses = ['Stark', 'Lannister', 'Targaryen', 'Greyjoy', 'Bolton']



		if post_data['kill_count'] < 0:
			error_msgs.append("You can't kill negative people, I think")

		if post_data['house'] not in houses:
			error_msgs.append("Not a real house.")

		if len(post_data['first_name']) < 4:
			error_msgs.append("First name is too short")
		elif len(post_data['first_name']) > 45:
			error_msgs.append('First name is too long')

		if error_msgs:
			# fail validations:
			return {
			'errors': error_msgs
			}
		else:
			# pass validation
			created_person = Person.objects.create(first_name=post_data['first_name'], last_name=post_data['last_name'], house=post_data['house'], favorite_weapon=post_data['fav_weapon'], deceased=post_data['deceased'], kill_count=post_data['kill_count'])
			return {
			'the_person': created_person
			}




class Person(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	house = models.CharField(max_length=45)
	deceased = models.BooleanField()
	favorite_weapon = models.CharField(max_length=45)
	kill_count = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = PersonManager()

