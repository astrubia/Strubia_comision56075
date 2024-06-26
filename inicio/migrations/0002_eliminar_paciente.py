# Generated by Django 5.0.2 on 2024-03-24 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='eliminar_paciente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('glucemia', models.IntegerField()),
                ('insulinoterapia', models.BooleanField(default=False)),
            ],
        ),
    ]
