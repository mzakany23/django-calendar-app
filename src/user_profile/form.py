from django.forms import ModelForm
from models import Profile

class ProfilePicUpload(ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
		