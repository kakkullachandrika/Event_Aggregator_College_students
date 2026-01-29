from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the home page")
def landing_page(request):
    return render(request, 'landing.html')
def sports(request):
    return render(request, 'sports.html')

def clubs(request):
    return render(request, 'clubs.html')

def placements(request):
    return render(request, 'placements.html')

def certifications(request):
    return render(request, 'certifications.html')