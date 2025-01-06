from django.contrib import admin
from .models import Category, Product, Supplier, Order, OrderItem, InventoryHistory


# Register your models here.
@admin.register(InventoryHistory)
class InventoryHistoryAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "action", "quantity_changed", "timestamp")
    list_filter = ("action", "timestamp")
    search_fields = ("product__name", "user__username")


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(OrderItem)
