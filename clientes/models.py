from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
	client = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Cliente")

	def __str__(self):
   		return self.client.username

