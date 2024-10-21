# Generated by Django 4.2.13 on 2024-10-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=20)),
                ('plant_name', models.CharField(max_length=100)),
                ('plant_price', models.IntegerField()),
            ],
            options={
                'db_table': 'plantdata',
            },
        ),
    ]