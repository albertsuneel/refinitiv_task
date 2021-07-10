from django.db import models


class User(models.Model):
    transaction_id = models.CharField(max_length=16)
    timestamp = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    currency = models.CharField(max_length=40)
    fx_rate_hq = models.CharField(max_length=20)
    fx_rate_spread = models.CharField(max_length=10)
    amount = models.CharField(max_length=20)
    branch_id = models.CharField(max_length=20)
    comments = models.CharField(max_length=500)
    status = models.IntegerField()

    class Meta:
        db_table = "user"

