# Generated by Django 5.1.1 on 2024-10-31 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_editora"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
