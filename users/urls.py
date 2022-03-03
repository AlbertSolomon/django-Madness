from unicodedata import name
from django.urls import path
from . import views

app_name = "users"
urlpatterns =[
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("login/addMe", views.addpassenger, name="addpassenger"),
    path("login/myFlights", views.myFlights, name = "myFlights"),
    
]