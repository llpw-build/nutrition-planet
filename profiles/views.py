from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import userRegisterForm
from.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect


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

@login_required
def profile(request):
    profile = request.user.user_profile

    if request.method == "POST":
        form = UserProfileForm(
            request.POST,
            instance=profile,
        )

    if form.is_valid():
            form.save()
    
            messages.success(
                request,
                "Your profile has been updated successfully.",
            )
    
            return redirect("profile")

    else:
        form = UserProfileForm(
            instance=profile,
        )

    context = {
        "form": form,
    }

    return render(
        request,
        "profiles/profile.html",
        context
    )