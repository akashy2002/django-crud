from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    return render(request, 'home.html')


def crudpage(request):
    if request.method == "POST":
        roll = request.POST.get('roll')
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('address')
        user = request.user

        c_obj = Crudcard(
            user=user,
            roll=roll,
            name=fname,
            email=email,
            phone=phone,
            address=add,
        )
        c_obj.save()
        redirect('crudpage')
    if request.user.is_authenticated:
        user = request.user
        info = Crudcard.objects.filter(user=user)
        return render(request, 'crud.html', {'info': info})

    return render(request, 'crud.html')


def update(request, id):
    if request.method == "POST":
        roll = request.POST.get('roll')
        fname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add = request.POST.get('address')
        user = request.user

        u_obj = Crudcard(
            id=id,
            roll=roll,
            name=fname,
            email=email,
            phone=phone,
            address=add,
            user=user,
        )

        u_obj.save()
        return redirect('crudpage')


def delete(request, id):
    dlt = Crudcard.objects.filter(id=id)
    dlt.delete()
    return redirect('crudpage')

# Authenticate APIs


def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']

        # user chcek validation-----
        if len(username) > 10:
            messages.error(request, 'Username should be under 10 characters')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match! Please try again')
            return redirect('home')

        # user create--
        myuser = User.objects.create_user(username, email, pass1)
        # myuser.first_name = fname
        # myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Congrats! Your account has been created ')
        return redirect('home')

    else:
        return render(request, 'signup.html')


def handleLogin(request):
    if request.method == "POST":
        lusername = request.POST['lusername']
        lpassword = request.POST['lpassword']

        user = authenticate(username=lusername, password=lpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Loged In')
            return redirect('home')

        else:
            messages.error(request, 'Sorry! Please Login')
            return redirect('LoginPage')

    else:
        return render(request, 'login.html')


def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully Loged Out')
    return redirect('LoginPage')
