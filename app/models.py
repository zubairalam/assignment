from django.db import models

# assuming a State can have multiple cities/places, each city can have multiple pincodes

class State(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    state = models.ForeignKey(State, null=False, blank=False, related_name='city')
    
    def __str__(self):
        return self.name

class Pincode(models.Model):
    name = models.CharField(max_length=6, null=False, blank=False, unique=True)
    city = models.ForeignKey(City, null=False, blank=False, related_name='pincode')

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    state = models.ForeignKey(State, related_name='profile_state', null=False, blank=False)
    city = models.ForeignKey(City, related_name='profile_city', null=False, blank=False)
    pincode = models.ForeignKey(Pincode, related_name='profile_pincode', null=False, blank=False)
    
    def __str__(self):
        return self.name
