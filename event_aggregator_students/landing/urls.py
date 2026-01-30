from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('landing/', views.landing_page, name='landing_page'), 
    path('sports/', views.sports, name='sports'),
    path('clubs/', views.clubs, name='clubs'),
    path('placements/', views.placements, name='placements'),
    path('certifications/', views.certifications, name='certifications'),
]