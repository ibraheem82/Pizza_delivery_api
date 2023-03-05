from django.contrib import admin
from .models import Order

# * Registering the Order model with the admin site.


@admin.register(Order)
# * Defining an admin class for the Order model.
class OrderAdmin(admin.ModelAdmin):
    # *  Specifying the fields to be displayed in the admin interface for the Order model.
    list_display = ['size', 'order_status', 'quantity', 'created_at']
    list_filter = ['created_at', 'order_status', 'size']
