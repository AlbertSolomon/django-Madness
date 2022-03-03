from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Passenger, Airport
#from django.views.generic import View
#from .process import htmlToPdf as pdfconverter
#from django.http import HttpResponse

# class based view
'''class GeneratePDF(View):
    def get(self, request, *args, **kwargs ):
        # getting the html template
        pdf = pdfconverter('flight.html')

        #rendering the html document
        return HttpResponse(pdf, content_type='application/pdf')'''


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id)
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

def pdfviewer(request):
    pass

