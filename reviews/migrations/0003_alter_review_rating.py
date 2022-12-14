# Generated by Django 4.1.1 on 2022-09-11 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(
                        5, "Ratings must be from 1 to 5"
                    )
                ]
            ),
        ),
    ]
