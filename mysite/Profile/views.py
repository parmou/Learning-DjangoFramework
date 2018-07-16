from django.shortcuts import render
from django.forms import ModelForm
from .forms import UserForm, UserProfileForm
# Create your views here. 

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)



def register(request):
	registered = False
	if request.method == 'POST':
		userform = UserForm(data = request.POST)
		userprofileform = UserProfileForm(data=request.POST)

		if userform.is_valid() and userprofileform.is_valid():
			user = userform.save()
			user.set_password(user.password)
			user.save()

			profile = userprofileform.save(commit = False)

			profile.user = user
			print(user)

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True

		else:
			print(userform.errors, userprofileform.errors)
	else:
		userform = UserForm()
		userprofileform = UserProfileForm()

	return render(request, 'Profile/register.html', {
		'userform' : userform,
		'userprofileform' :  userprofileform,
		'registered' : registered
		})
 

		