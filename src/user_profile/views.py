from django.shortcuts import render
from django.contrib.auth.models import User
from user_profile.models import Profile
from form import ProfileForm
from django.http import HttpResponseRedirect
from models import Profile
import re
from django import forms

def profile(request):
	try:
		profile = Profile.objects.get(id=request.user)
	except:
		profile = None
	context = {'profile' : profile}
	template = 'profile/index.html'
	return render(request,template,context)

def profile_update(request):
	form = ProfileForm(request.POST or None)
	if form.is_valid():
		print form.cleaned_data['email']
		form = ProfileForm()
	else:
		form = ProfileForm()

	if request.method == 'POST':
		pass
		# print request.POST['emailAddress']
	template = 'profile/_form.html'
	context = {'form' : form}
	return render(request,template,context)

def image_upload(request,id):
	validated = False

	try:
			upload = request.FILES['upload_file']
			file_name = str(upload)
			types = ['jpeg','png','img']
			extension = file_name[len(file_name)-4:len(file_name)].replace('.','')
			if extension in types:
				validated = True
				print 'worked'
	except:
			print "didn't work"
			upload = None

	if request.method == "POST":
		if upload and validated:
			try:
				profile = Profile.objects.get(account=id)
				user = User.objects.get(id=id)
				profile.image = upload
				profile.save()
			except:
				user = User.objects.get(id=id)
				profile= Profile(image=upload, account=user)
				profile.save()
		else:
			pass

	return HttpResponseRedirect('/profile/')