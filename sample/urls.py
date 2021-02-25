"""simple_MVC_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('about_us', views.about_us, name="about_us"),
    path('contact', views.contact, name="contact"),
    path('features', views.features, name="features"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('pricing', views.pricing, name="pricing"),
    path('services', views.services, name="services"),
    path('testimonials', views.testimonials, name="testimonials"),
    path('', views.index, name="index")
]
