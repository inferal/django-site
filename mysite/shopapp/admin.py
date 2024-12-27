from django.contrib import admin

from .models import Product, Order

class OrderInline(admin.TabularInline):
    model = Product.orders.through

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    list_display = "pk", "name", "description_short", "price", "discount"
    list_display_links = "pk", "name"
    ordering = "pk",
    search_fields = "name", "description"
    fieldsets = [
        (None, {
            "fields": ("name", "description"),
        }),
        ("Price options", {
            "fields": ("price", "discount"),
            "classes": ("wide", "collapse",) #скрывать не нужную дерикторию
        }),
        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Extra options. Field 'archived' is for soft delete",
        })
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 100:
            return obj.description
        return obj.description[:100] + "..."

class ProductInline(admin.TabularInline):
    model = Order.products.through

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "delivery_address", "promocode", "create_at", "user_verbose"
    ordering = "delivery_address",

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username