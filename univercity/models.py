from wsgiref.validate import validator
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class UniversityModel(models.Model):
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='images/univercity_logos')
    type = models.CharField(max_length=100)
    overview = models.TextField()
    since = models.IntegerField(validators=[MaxValueValidator(2022)])
    total_students = models.IntegerField()
    international_students = models.IntegerField()
    website_url = models.URLField(max_length=200)
    acceptance_rate = models.IntegerField()

    def __str__(self):
        return self.name