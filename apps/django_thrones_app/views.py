from django.shortcuts import render, redirect
from models import Person
from django.contrib import messages

# Create your views here.
def index(request):
	all_people = Person.objects.all()
	print all_people.query
	context = {
	'people':all_people
	}
	return render(request, 'django_thrones_app/index.html', context)

def create(request):
	if request.method == "POST":
		print request.POST
		# Without validation
		# Person.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], house=request.POST['house'], favorite_weapon=request.POST['fav_weapon'], deceased=request.POST['deceased'], kill_count=request.POST['kill_count'])

		# With Validation in a model manager
		validated_person = Person.objects.validate_person(request.POST)
		if 'errors' in validated_person:
			for validation_error in validated_person['errors']:
				messages.error(request, validation_error)
		if 'the_person' in validated_person:
			messages.success(request, "Wow, added "+validated_person['the_person'].first_name+ " " + validated_person['the_person'].last_name + "to die.")
		return redirect('/')