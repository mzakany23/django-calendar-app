from django.shortcuts import render
from models import Profile

def profile(request):
	profile = Profile.objects.get(id=request.user.id)
	context = {'profile' : profile}
	template = 'profile/index.html'
	return render(request,template,context)
