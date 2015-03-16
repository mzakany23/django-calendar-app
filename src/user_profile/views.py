from django.shortcuts import render
from django.contrib.auth.models import User
from user_profile.models import Profile
from form import ProfilePicUpload
from django.http import HttpResponseRedirect
from models import Profile
from form import ProfilePicUpload
import re

def profile(request):
	try:
		profile = Profile.objects.get(id=request.user)
	except:
		profile = None
	context = {'profile' : profile}
	template = 'profile/index.html'
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


	# 	file_name = str(upload)
	# 	types = ['jpeg','png','img']
	# 	extension = file_name[len(file_name)-4:len(file_name)].replace('.','')
		
	# 	if extension in types:
	# 		print upload
	# 		# upload.save(str(upload.replace(' ','')), upload, save=True)
	# 	else:
	# 		print 'cant upload'

	return HttpResponseRedirect('/profile/')