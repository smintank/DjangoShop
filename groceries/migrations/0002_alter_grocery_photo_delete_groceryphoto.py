# Generated by Django 5.0.6 on 2024-06-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groceries", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grocery",
            name="photo",
            field=models.ImageField(upload_to="products", verbose_name="Изображение"),
        ),
        migrations.DeleteModel(
            name="GroceryPhoto",
        ),
    ]