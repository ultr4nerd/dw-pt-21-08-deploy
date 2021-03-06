# Generated by Django 3.2.13 on 2022-06-17 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("me", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="programminglanguage",
            name="name",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Python"),
                    (1, "JavaScript"),
                    (2, "Java"),
                    (3, "C"),
                    (4, "C++"),
                    (5, "C#"),
                    (6, "PHP"),
                    (7, "Go"),
                    (8, "Rust"),
                    (9, "Dart"),
                    (10, "Elixir"),
                ]
            ),
        ),
    ]
