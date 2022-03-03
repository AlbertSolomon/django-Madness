from django.urls import path
from . import views
#from .views import GeneratePDF

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
    #path("pdf/", GeneratePDF.as_view(), name = "GeneratePDF"),
] 