# Generated by Django 5.0.3 on 2024-03-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wagon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('horaire_plan', models.CharField(max_length=50)),
                ('voyage', models.CharField(max_length=500)),
                ('img', models.CharField(max_length=5000)),
            ],
        ),
    ]