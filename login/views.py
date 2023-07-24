from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def register_request(request):
	if request.user.is_authenticated:
		return redirect("/questions")
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
			return redirect("/")
	form = NewUserForm()
	return render(request=request, template_name="login/register.html", context={"register_form":form})

def login_request(request):
	if request.user.is_authenticated:
		return redirect("/questions")
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("/questions")
	form = AuthenticationForm()
	return render(request=request, template_name="login/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	return redirect("/")