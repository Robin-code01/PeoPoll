from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
