from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                            'account/registration_done.html',
                            {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                    'account/register.html',
                    {'user_form': user_form})

def user_login(request):
    if request.method == 'POST': # when user submits form via POST
        form = LoginForm(request.POST) # instantiate form with submitted data
        if form.is_valid(): 

            # Authenticate user against database
            cd = form.cleaned_data 

            # Returns the User object if authentication successful
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user) # set the user in session
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    else: # when user_login view is called with a GET request
        form = LoginForm() # instantiate a new login form
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request,
                     'account/dashboard.html',
                     {'section': 'dashboard'})


from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                    'account/edit.html',
                    {'user_form': user_form,
                    'profile_form': profile_form})

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 
                'profile/profile_list.html',
                {"profiles" : profiles})
import datetime
@login_required
def profile(request, pk):
    profile = Profile.objects.get(user_id=pk)
    age = datetime.datetime.now().date() - profile.date_of_birth
    age = age.days // 365
    return render(request, 
                    "profile/profile.html", 
                    {"profile": profile,"age": age})
