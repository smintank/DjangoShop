from django.contrib import admin
from django.forms import ModelForm, ClearableFileInput

from groceries.models import Category, Grocery
from groceries.models import Subcategory


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 0
    fields = ("name", "slug", "image")
    show_change_link = True


class GroceryForm(ModelForm):
    class Meta:
        model = Grocery
        fields = ["name", "photo", "price"]
        widgets = {
            "photo": ClearableFileInput(),
        }


class GroceryInline(admin.TabularInline):
    model = Grocery
    form = GroceryForm
    extra = 0
    fields = ("name", "photo", "price")
    show_change_link = True


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "image")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [GroceryInline]
    list_filter = ("category",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "image")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [SubcategoryInline]


# class GroceryPhotoInline(admin.TabularInline):
#     model = GroceryPhoto
#     extra = 1
#     fields = ("original", "small", "medium", "large")


class GroceryAdmin(admin.ModelAdmin):
    list_display = ("name", "photo", "subcategory", "price")
    search_fields = ("name",)
    list_filter = ("subcategory",)
    ordering = ("name",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Grocery, GroceryAdmin)
