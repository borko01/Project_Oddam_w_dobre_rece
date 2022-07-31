from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, Http404, HttpResponse, JsonResponse
from .models import Donation, Category, Institution
from django.db.models import Sum, Count


# Create your views here.
class LandingPage(View):
    def get(self, request):
        donation = Donation.objects.aggregate(Sum("quantity"))
        institution = Institution.objects.count()
        foundation = Institution.objects.filter(type=1)
        ngo = Institution.objects.filter(type=2)
        local_collection = Institution.objects.filter(type=3)
        context = {
            "donation": donation,
            "institution": institution,
            "foundation": foundation,
            "ngo": ngo,
            "local": local_collection
        }
        return render(request, "index.html", context)


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        return render(request, "register.html")
