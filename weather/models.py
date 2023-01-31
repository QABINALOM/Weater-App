from django.db import models
from Weatherapp2 import settings

class City(models.Model):
    name = models.CharField(max_length=30)
    
    def save(self, *args, **kwargs):
        if City.objects.count() < int(settings.MAX_CITY_COUNT):
            super().save(*args, **kwargs)
        else:
            for city in City.objects.filter():
                City.objects.filter(name=city).delete()
                super().save(*args, **kwargs)
                break

    def __str__(self):
        return self.name
