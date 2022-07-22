from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, Http404, HttpResponse


# Create your views here.
class LandingPage(View):
    def get(self, request):
        return render(request, "index.html")


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        return render(request, "register.html")
