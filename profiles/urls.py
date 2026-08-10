from django.urls import path, include
from . import views

urlpatterns = [
    
    path("",
        views.profile, 
        name="profile"
    ),

    path(
        "register/",
        views.register,
        name="register",
    ),
]   