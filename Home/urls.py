from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
        path("",views.index,name='Home'),
        path("about",views.about,name='about'),
        path("contact",views.contact,name='contact'),
        path('form',views.form,name="form"),
        path('dashboard',views.dashboard,name="dashboard"),
        path('file',views.file,name="file")
]

