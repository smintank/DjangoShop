from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from groceries.models import Category, Grocery
from groceries.serializers import CategorySerializer, GrocerySerializer


# class CategoryView(ListView):
#     model = Category
#     queryset = model.objects.select_related("subcategories").all()
#     paginate_by = 10
#
#
# class GroceryView(ListView):
#     model = Grocery
#     queryset = model.objects.select_related(
#         "subcategory", "subcategory__category"
#     ).all()
#     paginate_by = 10


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GroceryViewSet(viewsets.ModelViewSet):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
