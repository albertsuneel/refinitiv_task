from django.db import models


class Rates(models.Model):
    currency = models.CharField(max_length=3)
    rate = models.FloatField()
    spread = models.FloatField()

    class Meta:
        db_table = "rates"


class Branches(models.Model):
    branch_id = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=40)
    address_line2 = models.CharField(max_length=40)
    address_line3 = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)

    class Meta:
        db_table = "branches"


class Manager(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=15)

    class Meta:
        db_table = "manager"


