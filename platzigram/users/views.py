""" Users views """
#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Excepcions
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User

from users.models import Profile


def login_view(request):
    """Login view"""
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed') #Acording to name used in urls.py
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')

def update_profile(request):
    return render(request, 'users/update_profile.html')

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Passwords does not match'})

        #Here the user is created
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'This username already exists'})
        #After, we add the other data
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save() #If we don't user Profile.object.Create_user, we need to put save in another line

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required()
def logout_view(request):
    """ Logout a user"""
    logout(request)
    return redirect('login')