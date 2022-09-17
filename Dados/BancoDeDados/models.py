from django.db import models

# Create your models here.

class Dados(models.Model):

    Nome = models.CharField(max_length=255)
    Valor = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
