# Generated by Django 5.1.2 on 2024-10-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
