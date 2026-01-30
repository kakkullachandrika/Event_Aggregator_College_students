from django.shortcuts import render
from django.http import HttpResponse 
from .models import Certification , Club
# Create your views here.
def home(request):
    featured_event = Event.objects.order_by('-date').first()
    context = {
        'featured': featured_event,
        'sports_count': Event.objects.filter(category='Sports').count(),
        'clubs_count': Event.objects.filter(category='Clubs').count(),
        'placements_count': Event.objects.filter(category='Placements').count(),
        'certifications_count': Event.objects.filter(category='Certifications').count(),
        'upcoming_events': Event.objects.order_by('date')[:5],
    }
    return render(request, 'landing.html', context)

def landing_page(request):
    return render(request, 'landing.html')
def sports(request):
    return render(request, 'sports.html')

def clubs(request):
    if request.method=='POST':
        event_name =request.POST.get('event_name ')
        event_category=request.POST.get('event_category')
        date_and_time=request.POST.get('date_and_time')
        venue=request.POST.get('venue')
        organizer=request.POST.get('organizer')
        registration_link=request.POST.get('registration_link')
        cer=Club(event_name=event_name, event_category= event_category, date_and_time= date_and_time,venue=venue,organizer=organizer,registration_link=registration_link)
        cer.save()
    c=Club.objects.all().order_by('-id')
    return render(request , 'clubs.html',{'club':c})

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
    from django.shortcuts import redirect
# footer
def facebook_page(request):
    return redirect("https://www.facebook.com/sphoorthyengineeringcollege")

def instagram_page(request):
    return redirect("https://www.instagram.com/sphoorthyengineeringcollege")

def twitter_page(request):
    return redirect("https://twitter.com/sphoorthycollege")

def whatsapp_page(request):
    return redirect("https://wa.me/919999999999")

    return render(request , 'certifications.html',{'certification':c})
   
