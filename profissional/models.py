from django.db import models

# Create your models here.
class Especialidade(models.Model):
    
    especialidade_choices = {
        ('Acupuntura', 'Acupuntura'),
        ('F.Aquática', 'F.Aquática'),
        ('F.Cardiovascular', 'F.Cardiovascular'),
        ('F.Esportiva', 'F.Esportiva'),
    }
    especialidade = models.CharField(max_length=100,choices=especialidade_choices, default='Acuputura')
    
    def __str__(self):
        return self.especialidade
    
class Profissional(models.Model):

    nome = models.CharField(max_length=255)
    area_especializacao = models.ManyToManyField(Especialidade)
    telefone = models.CharField(max_length=20)
    
    email = models.EmailField()

    def __str__(self):
        return self.nome
