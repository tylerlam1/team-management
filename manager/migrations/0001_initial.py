# Generated by Django 4.0 on 2021-12-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teammate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
