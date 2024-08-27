# Generated by Django 5.1 on 2024-08-27 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0003_alter_profissional_especialidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='especialidade',
            field=models.CharField(choices=[('F.Cardiovascular', 'F.Cardiovascular'), ('Acupuntura', 'Acupuntura'), ('F.Esportiva', 'F.Esportiva'), ('F.Aquática', 'F.Aquática')], default='Acunputura', max_length=100),
        ),
    ]
