from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)  # this will create a form with data has been in the POST request
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect('blog-home')
        else:
            form = UserRegisterForm()
    else:
        form = UserRegisterForm()
    form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})