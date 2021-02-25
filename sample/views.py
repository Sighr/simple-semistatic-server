from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html", {"active": "index"})


def contact(request):
    return render(request, "contact.html", {"active": "contact"})


def features(request):
    return render(request, "features.html", {"active": "features"})


def about_us(request):
    return render(request, "about_us.html", {"active": "about_us"})


def portfolio(request):
    return render(request, "portfolio.html", {"active": "portfolio"})


def pricing(request):
    return render(request, "pricing.html", {"active": "pricing"})


def services(request):
    return render(request, "services.html", {"active": "services"})


def testimonials(request):
    return render(request, "testimonials.html", {"active": "testimonials"})
