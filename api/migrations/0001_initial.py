# Generated by Django 3.1.1 on 2020-10-03 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=70)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
