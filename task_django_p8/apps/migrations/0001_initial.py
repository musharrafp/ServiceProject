# Generated by Django 4.2 on 2023-04-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[('1', 'Sedan'), ('2', 'Truck'), ('4', 'SUV')])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('years_ago', models.PositiveIntegerField()),
            ],
        ),
    ]
