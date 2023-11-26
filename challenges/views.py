from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge = "None"
    if month == "january":
        challenge = "Eat not meat for the entire month !"
    elif month == "february":
        challenge = "Walk for at least 20 minutes everyday !"
    elif month == "march":
        challenge = "Learn for at least 20 minutes everyday !"
    else:
        return HttpResponseNotFound("This month is not supported !")

    return HttpResponse(challenge)
