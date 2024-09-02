from django.db import models

# Create your models here.
class Registradores(models.Model):
    nome = models.CharField(max_length=60, null=False)
    email = models.EmailField(null=False)
    senha = models.CharField(max_length=64,null=False)
    
    
    def __str__(self):
        return self.nome