from django.db import models


class User(models.Model):

    def __str__(self) -> str:
        return self.id


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    phone_num = models.CharField(10)

    def __str__(self) -> str:
        return self.name
