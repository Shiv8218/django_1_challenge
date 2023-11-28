from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months":months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text":challenge_text,
            "month" : month
        })
    except:
        raise Http404()
