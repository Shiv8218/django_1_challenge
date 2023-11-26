from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Eat not meat for the entire month !",
    "february": "Walk for at least 20 minutes everyday !",
    "march": "Learn for at least 20 minutes everyday !",
    "april": "Eat not meat for the entire month !",
    "may": "Eat not meat for the entire month !",
    "june": "Walk for at least 20 minutes everyday !",
    "july": "Eat not meat for the entire month !",
    "august": "Learn for at least 20 minutes everyday !",
    "september": "Eat not meat for the entire month !",
    "october": "Eat not meat for the entire month !",
    "november": "Eat not meat for the entire month !",
    "december": "Learn for at least 20 minutes everyday !"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported !")
    