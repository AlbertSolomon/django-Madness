from ast import arg
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from flights.models import Passenger, Flight   

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))
    return render(request,"users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        #view_userflight = Passenger.objects.filter(firstname=username)

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))

        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials !",
                #"user_flight": view_userflight,             
            })

    return render(request, "users/login.html")

def addpassenger(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        
        name  = Passenger.objects.all()
        passenger_name = name.filter(firstname=firstname, lastname=lastname)
        query_result = passenger_name.count()

        #getting the id of the passenger
        nameOfpassenger = name.get(firstname=firstname, lastname=lastname)
        passenger_id = nameOfpassenger.id

        #tracking the flights the passenger has booked 
        all_flights = Flight.objects.all()
        my_flights = all_flights.filter(passengers = passenger_id)

        if query_result != 1:
            name = Passenger.objects.create(firstname=firstname, lastname=lastname)
            name.save()
            message = "Passenger added successfully"

            return render(request, "users/user.html",{
                "message": message,
                "my_flights": my_flights,
            
            })
        
    return render(request, "users/user.html",{
        "message": "unable to join the passenger list",
        "my_flights": my_flights,
    })

#display the flights the user has booked
def myFlights(request, passenger_id):
    pass

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out !!"
    })