from django.urls import path

from carts.views import (
    CartSummeryView,
    CartEmptyView,
    CartAddItemView,
    CartRemoveItemView,
    CartUpdateItemView,
)

app_name = "cart"

urlpatterns = [
    path("show/", CartSummeryView.as_view(), name="show_all"),
    path("empty/", CartEmptyView.as_view(), name="empty"),
    path("add/<slug:grocery_slug>", CartAddItemView.as_view(), name="add_item"),
    path(
        "remove/<slug:grocery_slug>",
        CartRemoveItemView.as_view(),
        name="remove_item",
    ),
    path(
        "update/<slug:grocery_slug>",
        CartUpdateItemView.as_view(),
        name="update_item",
    ),
]
