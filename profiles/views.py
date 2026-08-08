from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)

           messages.success(
               request,
                "Welcome to Planet Nutrition! Your account has been created successfully.",
            )

           return redirect("home")

    else:

        form = UserRegisterForm()

    context = {
        "form": form,
    }

    return render(
    request,
    "registration/register.html",
    context,
)