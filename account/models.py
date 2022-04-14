from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ExtendUser(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    contact = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' ' + str(self.firstname) + ' ' + str(self.lastname)