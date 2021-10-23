from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from Eccomerce.catalog.models import Item


class Coupon(models.Model):
    user:models.ForeignKey = models.ForeignKey(User,on_delete=models.CASCADE)
    coupon_cost:models.IntegerField = models.IntegerField(default=0)
    all_items:models.BooleanField = models.BooleanField(default=False)
    item:models.ForeignKey = models.ForeignKey(Item)
    created:models.DateTimeField = models.DateTimeField(auto_created=True)
    expired:models.DateTimeField = models.DateTimeField()

    def check_if_expired(self):
        if datetime.now() <= self.expired:



