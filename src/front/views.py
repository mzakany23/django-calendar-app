from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect
from form import LoginForm

@login_required
def home(request):
	if request.user.is_authenticated():
		context = {}
		template = 'home/index.html'
		return render(request,template,context)
	else:
		HttpResponseRedirect('/auth_login/')

def auth_login(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username,password=password)
		
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('/')

	context = {'form' : form}
	template = 'home/login.html'
	return render(request,template,context)


def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/')