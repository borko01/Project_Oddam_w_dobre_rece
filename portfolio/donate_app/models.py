from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.TextField()


TYPE = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna")
)


class Institution(models.Model):
    name = models.CharField(max_length=123),
    description = models.TextField(),
    type = models.IntegerField(choices=TYPE, default=1),
    category = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField,
    categories = models.ManyToManyField(Category),
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE),
    address = models.CharField(max_length=168),
    phone_number = models.IntegerField,
    city = models.CharField(max_length=128),
    zip_code = models.CharField(max_length=10),
    pick_up_date = models.DateField,
    pick_up_time = models.TimeField,
    pick_up_comment = models.TextField(null=True),
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
