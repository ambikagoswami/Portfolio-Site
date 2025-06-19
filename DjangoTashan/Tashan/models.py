from django.db import models
from django.utils import timezone

# Create your models here.

class TashanVariety(models.Model):
    TASHAN_TYPE_CHOICE = [
        ('SH','SHERNI'),
        ('BN','BINDAAS'),
        ('NV','NAVAV'),
        ('DB','DABANG'),
        ('TR','TEWAR'),
    ]

    name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='tashans/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=TASHAN_TYPE_CHOICE)

    def __str__(self):
        return self.name