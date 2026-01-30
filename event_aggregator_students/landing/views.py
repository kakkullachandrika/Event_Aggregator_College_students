from django.shortcuts import render
from django.http import HttpResponse 
from .models import Certification
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
    if request.method=='POST':
        event_name =request.POST.get('event_name ')
        event_category=request.POST.get('event_category')
        date_and_time=request.POST.get('date_and_time')
        venue=request.POST.get('venue')
        organizer=request.POST.get('organizer')
        registration_link=request.POST.get('registration_link')
        cer=Certification(event_name=event_name, event_category= event_category, date_and_time= date_and_time,venue=venue,organizer=organizer,registration_link=registration_link)
        cer.save()
    c=Certification.objects.all().order_by('-id')
    return render(request , 'certifications.html',{'certification':c})
   