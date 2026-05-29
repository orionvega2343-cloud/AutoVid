from django.contrib import admin
from .models import CarModel, Brand, Part, Order

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'generation']
    list_filter = ['brand']
    search_fields = ['brand', 'name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name']

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['sku', 'brand', 'name', 'category', 'price', 'in_stock', 'is_active']
    list_editable = ['price', 'in_stock', 'is_active']
    search_fields = ['sku', 'name', 'brand__name']
    list_filter = ['brand', 'category', 'is_active']
    filter_horizontal = ('applicable_cars',)
    fieldsets = [
        (
            "Основная информация",
            {
                "fields": ("sku", "name", "brand", "category"),
            },
        ),
        (
            "Цены и склад",
            {
                "fields": ("price", "price_old", "in_stock"),
            },
        ),
        (
            "Применимость",
            {
                "fields": ("applicable_cars",),
            },
        ),
        (
            "Логистика",
            {
                "fields": ("weight_kg", "hs_code"),
            },
        ),
        (
            "Медиа и статус",
            {
                "fields": ("image", "is_active"),
            },
        ),
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'part', 'client_name', 'client_phone', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['client_name', 'client_phone', 'part__name']
    readonly_fields = ['created_at', 'updated_at']