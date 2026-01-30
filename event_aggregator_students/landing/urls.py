from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('landing/', views.landing_page, name='landing_page'), 
    path('sports/', views.sports, name='sports'),
    path('clubs/', views.clubs, name='clubs'),
    path('placements/', views.placements, name='placements'),
    path('certifications/', views.certifications, name='certifications'),
    path('add-event/', views.add_event, name='add_event'),
    path("social/facebook/", views.facebook_page, name="facebook"),
    path("social/instagram/", views.instagram_page, name="instagram"),
    path("social/twitter/", views.twitter_page, name="twitter"),
    path("social/whatsapp/", views.whatsapp_page, name="whatsapp"),

]
