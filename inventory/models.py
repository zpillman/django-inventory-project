from django.db import models


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

    def __str__(self):
        return str(self.name) + ", " + str(self.location)


class Part(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=50)
    on_hand = models.IntegerField()
    price = models.FloatField()
    min = models.IntegerField()
    max = models.IntegerField()


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=50)
    parts = models.ManyToManyField(Part)
    on_hand = models.IntegerField()
    price = models.FloatField()
    min = models.IntegerField()
    max = models.IntegerField()
