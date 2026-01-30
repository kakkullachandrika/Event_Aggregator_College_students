from django.db import models

# Create your models here.
class Certification(models.Model):
    event_name = models.CharField(max_length=200)
    event_category = models.CharField(max_length=100)
    date_and_time=models.DateTimeField()
    venue=models.CharField()
    organizer=models.CharField()
    registration_link=models.CharField()