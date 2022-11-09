from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Country name')
    code = models.CharField(max_length=2, verbose_name='Country code')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='City name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name='Country')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class University(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='universities', verbose_name='City')
    name = models.CharField(max_length=100, verbose_name='University name')
    acronym = models.CharField(max_length=10, verbose_name='University acronym')
    logo = models.ImageField(upload_to='images/university_logos', verbose_name='University logo')
    type = models.CharField(max_length=100, verbose_name='University type')
    overview = models.TextField(verbose_name='University overview')
    since = models.IntegerField(validators=[MaxValueValidator(2022)], verbose_name='University since')
    total_students = models.IntegerField(verbose_name='Total students')
    international_students = models.IntegerField(verbose_name='International students')
    website_url = models.URLField(max_length=200, verbose_name='University website url')
    acceptance_rate = models.IntegerField(verbose_name='Acceptance rate')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Universities'