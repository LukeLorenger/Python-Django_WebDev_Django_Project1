from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # New user form
from django.contrib import messages # What type of message we would like to add

# register view FUNCTION
def register(request):
	if request.method == 'POST': # If we get post request, we will validate form data
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save() # Save User
			username = form.cleaned_data.get('username') # If valid, grab username
			messages.success(request, f'Account created for {username}!') # Flashed message using F string
			return redirect('blog-home') # name we gave to URL pattern for blog home page

	else: # if not, display blank form
		form = UserCreationForm() # Instance of the form
	return render(request, 'users/register.html', {'form': form}) # render template that uses this form, uses instance


# The diff types of messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error


