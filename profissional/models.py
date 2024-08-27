from django.db import models

# Create your models here.
class Profissional(models.Model):
    especialidade_choices = {
        ('Acupuntura', 'Acupuntura'),
        ('F.Aquática', 'F.Aquática'),
        ('F.Cardiovascular', 'F.Cardiovascular'),
        ('F.Esportiva', 'F.Esportiva'),
    }
    
    nome = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=100,choices=especialidade_choices, default='Acunputura')
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome
