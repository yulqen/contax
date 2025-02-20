# Generated by Django 5.1.6 on 2025-02-16 12:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(blank=True, max_length=254)),
                (
                    "mobile_phone",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("website", models.URLField(blank=True)),
                ("twitter_handle", models.CharField(blank=True, max_length=15)),
                ("linkedin_profile", models.URLField(blank=True)),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("address", models.TextField(blank=True)),
                ("notes", models.TextField(blank=True)),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="contacts/photos/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_favorite", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ["last_name", "first_name"],
            },
        ),
    ]
