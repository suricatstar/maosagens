from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from paciente.models import Paciente
from profissional.models import Especialidade, Profissional

# Create your models here.
class Agendamento(models.Model):
    HORARIOS = (
        ("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),
    )
    
    def validar_dia(value):
        today = date.today()
        weekday = date.fromisoformat(f'{value}').weekday()

        if value < today:
            raise ValidationError('Não é possivel escolher um data atrasada.')
        
        if (weekday == 5) or (weekday == 6):
            raise ValidationError('Escolha um dia útil da semana.')
    
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    profissional = models.ForeignKey(Profissional, on_delete=models.DO_NOTHING)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.DO_NOTHING)
    data = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia], default=date.today())
    hora = models.CharField(max_length=60, choices=HORARIOS)
    
    class Meta:
        verbose_name = 'Agenda'
        
    def __str__(self):
        return f"{self.paciente} | {self.profissional}"
    