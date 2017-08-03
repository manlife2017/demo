from django.db import models


# Create your models here.
class PeopleResurne(models.Model):
    ima_url = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    birthday = models.CharField(max_length=30)
    identityCard = models.CharField(max_length=20)
    identityNum = models.CharField(max_length=18)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=40)
    other = models.TextField(max_length=500)
    ctime = models.DateTimeField(auto_now=True)


class Education(models.Model):
    people = models.ForeignKey('PeopleResurne')
    school = models.CharField(max_length=40)
    educationTitle = models.TextField(max_length=1600)


class Work(models.Model):
    people = models.ForeignKey('PeopleResurne')
    workTimeStart = models.CharField(max_length=20)
    workTimeEnd = models.CharField(max_length=20)
    workUnit = models.CharField(max_length=40)
    workTitle = models.TextField(max_length=1600)
