# Generated by Django 5.1.1 on 2024-09-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="networknode",
            name="country",
            field=models.CharField(max_length=100, verbose_name="Страна"),
        ),
    ]
