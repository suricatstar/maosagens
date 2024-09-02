from django.db import models

# Create your models here.
class Especialidade(models.Model):
    
    especialidade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.especialidade
    
class Profissional(models.Model):

    nome = models.CharField(max_length=255)
    area_especializacao = models.ForeignKey(Especialidade, on_delete=models.DO_NOTHING)
    telefone = models.CharField(max_length=20)
    
    email = models.EmailField()

    def __str__(self):
        return self.nome
