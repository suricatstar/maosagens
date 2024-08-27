from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=60, null=False)
    email = models.EmailField(null=False)
    senha = models.CharField(max_length=20,null=False)
    telefone = models.CharField(max_length=15, null=True,blank=True)
    data_nascimento = models.DateField(null=True,blank=True)
    
    
    def __str__(self):
        return self.nome