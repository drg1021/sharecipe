from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from . models import User

# Create your views here.

def default(request):
    return render(request, "users/default.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("Success")
            login(request, user)
        else:
            print("Failed")
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]

        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return redirect("user:login")
    return render(request, "users/signup.html")