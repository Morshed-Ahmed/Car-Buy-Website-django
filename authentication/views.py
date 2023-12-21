from django.shortcuts import render,redirect
from .forms import RegisterUser,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from car.models import Car,CarBuy
from brand.models import Brand

# Create your views here.
def UserSignup(request):

    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
            print(form.cleaned_data)
    else:
        form = RegisterUser()
    return render(request, './signup.html', {'form': form})

def UserLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                return redirect('profile') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def LogOut(request):
    logout(request)
    return redirect('login')


def profile(request):
    car_data = CarBuy.objects.filter(name =request.user)
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
    else:
        form = ChangeUserData(instance=request.user)
    
    return render(request,'profile.html',{'car_data':car_data,'form':form})