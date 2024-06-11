from base64 import b64decode

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.fields import ImageField

from groceries.models import Category, Grocery, Subcategory


class Base64ImageField(ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(b64decode(imgstr), name="temp." + ext)
        return super().to_internal_value(data)

    def to_representation(self, value):
        return self.context["request"].build_absolute_uri(value.url)


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"


class GrocerySerializer(serializers.ModelSerializer):
    photo = Base64ImageField()
    subcategory = serializers.SlugRelatedField(
        queryset=Subcategory.objects.all(),
        slug_field="name",
    )
    category = serializers.CharField(source="subcategory.category.name", read_only=True)

    class Meta:
        model = Grocery
        fields = (
            "name",
            "slug",
            "photo",
            "subcategory",
            "category",
            "price",
        )
