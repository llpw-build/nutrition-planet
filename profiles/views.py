from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import userRegisterForm

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        messages.info(
            request,
            "You are already logged in.",
        )
        return redirect("home")

    if request.method == "POST":
        form = userRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Welcome to Planet Nutrition! Your account has been created successfully.",
            )

            return redirect("home")

    else:
        form = userRegisterForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "registration/register.html",
        context,
    )