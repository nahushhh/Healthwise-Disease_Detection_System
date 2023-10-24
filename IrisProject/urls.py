"""IrisProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from IrisApp.views import diseasePrediction, firstAid , doctorRecommendation,docMaps
from auapp.views import user_login , user_signup , user_logout , landing , contact
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", diseasePrediction, name="home" ),
    path("firstAid/", firstAid, name="firstAid"),
    path("maps/", docMaps, name="maps"),
    path("docRecommend/", doctorRecommendation, name="docRecommend"),
    path("user_login/", user_login, name="user_login"),
    path("user_signup/", user_signup, name="user_signup"),
    path("user_logout/", user_logout, name="user_logout"),
    path("landing/", landing, name="landing"),
    path("contact/", contact, name="contact"),
    
    
    
]
