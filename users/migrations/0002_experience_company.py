# Generated by Django 4.2.5 on 2023-09-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
