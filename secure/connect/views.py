from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignInForm
from .forms import SignUpForm


def SignIn(request):
    message = ""
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'form':form, 'message':'Vous êtes connecté'})
            else:
                return render(request, 'index.html', {'form':form, 'message':"Vous n'avez pas reussit à vous connecter"})
    else:
        form = SignInForm()
          
    return render(request, 'index.html', {'form':form, 'message':message})

def SignUp(request):
    message=""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('signin')
        else:
            message = "L'inscription a échoué"
            return render(request, 'index.html', {'form':form, 'message':message})
    else:
        form = SignUpForm()
          
    return render(request, 'index.html', {'form':form, 'message':message})