from django.contrib.auth.models import User
from django.db import models


class BaseCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(
        upload_to="categories", blank=True, verbose_name="Изображение", max_length=255
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(BaseCategory):
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"


class Subcategory(BaseCategory):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="subcategories",
    )

    class Meta:
        verbose_name = "подкатегория"
        verbose_name_plural = "Подкатегории"


# class GroceryPhoto(models.Model):
#     original = models.ImageField(upload_to="products", verbose_name="Изображение")
#     small = models.ImageField(
#         upload_to="products", verbose_name="Маленькое изображение"
#     )
#     medium = models.ImageField(upload_to="products", verbose_name="Среднее изображение")
#     large = models.ImageField(upload_to="products", verbose_name="Большое изображение")


class Grocery(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField(upload_to="products", verbose_name="Изображение")
    subcategory = models.ForeignKey(
        Subcategory, null=True, on_delete=models.SET_NULL, verbose_name="Подкатегория"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "Продукты"
