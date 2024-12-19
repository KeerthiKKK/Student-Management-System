# Generated by Django 5.1.4 on 2024-12-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_no', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('Degree', models.CharField(max_length=30)),
                ('CGPA', models.FloatField()),
            ],
        ),
    ]