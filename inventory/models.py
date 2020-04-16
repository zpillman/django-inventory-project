from django.db import models


class Part(models.Model):
    name = models.CharField(max_length=50)
    on_hand = models.IntegerField()
    price = models.IntegerField()
    min = models.IntegerField()
    max = models.IntegerField()


class Company(models.Model):
    CONTINENTS = (('AF', 'Africa'),
                  ('NA', 'North America'),
                  ('OC', 'Oceania'),
                  ('AN', 'Antarctica'),
                  ('AS', 'Asia'),
                  ('EU', 'Europe'),
                  ('SA', 'South America'))

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=2, choices=CONTINENTS, default='NA')


