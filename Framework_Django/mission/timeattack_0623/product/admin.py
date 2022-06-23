from django.contrib import admin

from .models import orders, categories, item_orders, items

admin.site.register(orders)
admin.site.register(categories)
admin.site.register(item_orders)
admin.site.register(items)
