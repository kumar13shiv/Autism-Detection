from django.shortcuts import render, redirect, HttpResponse
from .forms import ProfileForm, UpdateProfileForm, UserCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
# from django.contrib.auth.decorators import login_required


def homepage(request):
    return HttpResponse('<h1>Home Page</h1>')
    # return render(request, "home.html", {'user': request.user})


def register(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            name = profile_form.cleaned_data["name"]
            mail = profile_form.cleaned_data["mail"]
            age = profile_form.cleaned_data["age"]
            gender = profile_form.cleaned_data["gender"]
            user = User.objects.get(username=user_form.cleaned_data["username"])
            p = UserProfile(user=user, name=name, mail=mail, age=age, gender=gender)
            p.save()
            return redirect("/login")
        else:
            return HttpResponse('<h1>Invalid Form</h1>')
    else:
        user_form = UserCreateForm()
        profile_form = ProfileForm()

    # return HttpResponse('<h1>Sign Up Form</h1>')
    return render(request, "register.html", {'user_form': user_form, 'profile_form': profile_form})