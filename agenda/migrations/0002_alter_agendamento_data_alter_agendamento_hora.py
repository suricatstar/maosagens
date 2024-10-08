# Generated by Django 5.1 on 2024-09-02 03:09

import agenda.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data',
            field=models.DateField(default=datetime.date(2024, 9, 2), help_text='Insira uma data para agenda', validators=[agenda.models.Agendamento.validar_dia]),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='hora',
            field=models.CharField(choices=[('1', '07:00 ás 08:00'), ('2', '08:00 ás 09:00'), ('3', '09:00 ás 10:00'), ('4', '10:00 ás 11:00'), ('5', '11:00 ás 12:00')], max_length=60),
        ),
    ]
