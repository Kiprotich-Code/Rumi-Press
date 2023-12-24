from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            print('User does not exist')

    else:
        return render(request, 'users/signin.html', {})


def signout(request):
    logout(request)
    return redirect('index')

@login_required()
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        

    else:
        form = ProfileForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'users/update_profile.html', context)


@login_required()
def view_profile(request, id):
    prof = User.objects.get(pk=id)
    context={'prof':prof}
    return render(request, 'users/view_profile.html', context)