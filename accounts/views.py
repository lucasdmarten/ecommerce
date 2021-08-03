from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, render

from accounts import tools
from accounts.forms import CreateUserForm, LoginUserForm
from accounts.models import MyUser


def register_page(request):
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            password = form.clean_password2()
            user = form.save()
            return redirect('login')
    else:
        form = CreateUserForm()

    return render(request, 'accounts/register.html', {"form":form})

def login_page(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            data = tools.get_data(form, register=False)
            if MyUser.objects.filter(email=data['email']).exists():
                user = authenticate(email=data['email'],
                                    password=data['password'])
                if user is not None:
                    login(request, user)
                    print('user is authenticated...')
                    return redirect('store')
        
    
    else:
        form = LoginUserForm()
        print('user isnt authenticated')

    return render(request, 'accounts/login.html', {"form":form})

def logout_page(request):
    logout(request)
    return redirect('login')



    
