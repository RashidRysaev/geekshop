# Generated by Django 2.2.18 on 2021-02-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_auto_20210218_1136"),
    ]

    operations = [
        migrations.AddField(
            model_name="productcategory",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="категория активна"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, verbose_name="описание продукта"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=128, verbose_name="имя продукта"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name="цена продукта"),
        ),
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(default=0, verbose_name="количество на складе"),
        ),
        migrations.AlterField(
            model_name="product",
            name="short_desc",
            field=models.CharField(blank=True, max_length=60, verbose_name="краткое описание продукта"),
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="description",
            field=models.TextField(blank=True, verbose_name="описание"),
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="name",
            field=models.CharField(max_length=64, unique=True, verbose_name="имя"),
        ),
    ]
