# Generated by Django 4.1.7 on 2023-03-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Links",
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
                ("link_original", models.URLField()),
                ("link_encurtado", models.CharField(max_length=8)),
            ],
        ),
    ]