# Generated by Django 4.2.13 on 2024-07-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=50)),
                ('emb_dob', models.DateTimeField()),
                ('emp_address', models.CharField(max_length=200)),
            ],
        ),
    ]
