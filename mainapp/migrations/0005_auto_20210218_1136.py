# Generated by Django 2.2.18 on 2021-02-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_fill_db"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="address",
            field=models.CharField(max_length=254, verbose_name="адресс"),
        ),
    ]
