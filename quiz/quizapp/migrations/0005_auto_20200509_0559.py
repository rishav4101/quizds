# Generated by Django 3.0.6 on 2020-05-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_myusers_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
