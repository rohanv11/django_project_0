# Generated by Django 5.1.2 on 2024-10-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_students_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
