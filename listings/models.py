from django.contrib.gis.db import models


class Listing(models.Model):
    name = models.CharField(max_length=50, null=False,
                            verbose_name="name of the listing")
    price = models.IntegerField(
        verbose_name="price of the listing", null=False)
    date_listed = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    property = models.OneToOneField(Listing, on_delete=models.CASCADE)
    county = models.CharField(max_length=40)
    location = models.PointField(srid=21096)
