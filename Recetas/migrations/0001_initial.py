# Generated by Django 5.0.1 on 2024-11-30 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receta', models.CharField(max_length=300)),
                ('paciente', models.IntegerField()),
                ('oftalmologo', models.IntegerField()),
            ],
        ),
    ]