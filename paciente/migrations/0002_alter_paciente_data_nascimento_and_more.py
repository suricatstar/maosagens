# Generated by Django 5.1 on 2024-08-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
