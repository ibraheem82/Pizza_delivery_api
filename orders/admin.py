from django.contrib import admin
from .models import Order

# * Registering the Order model with the admin site.


@admin.register(Order)
# * Defining an admin class for the Order model.
class OrderAdmin(admin.ModelAdmin):
    # *  Specifying the fields to be displayed in the admin interface for the Order model.
    list_display = ['size', 'order_status', 'quantity', 'date_purchased']
    # * Adding filters to the admin interface for the Order model based on the specified fields.
    list_filter = ['date_purchased', 'order_status', 'size']
