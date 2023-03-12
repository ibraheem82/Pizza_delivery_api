# import models from django
from django.db import models

# import get_user_model from django.contrib.auth to get the User model defined in settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model

# set User variable to the User model defined in settings.AUTH_USER_MODEL
User = get_user_model()

# Create Order model


class Order(models.Model):
    # create choices tuple for sizes
    SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA_LARGE', 'extraLarge'),
    )

    # create choices tuple for order status
    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'inTransit'),
        ('DELIVERED', 'delivered'),
    )

    # create foreign key relationship to the User model
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # set size as a char field with max length of 25 and default to the first option in the SIZES tuple
    size = models.CharField(max_length=25, choices=SIZES, default=SIZES[0][0])
    # set order status as a char field with max length of 25 and default to the first option in the ORDER_STATUS tuple
    order_status = models.CharField(
        max_length=25, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    # set quantity as an integer field
    quantity = models.IntegerField()
    # set created_at as a DateTimeField with auto_now_add set to True to automatically add creation timestamp
    date_purchased = models.DateTimeField(auto_now_add=True)
    # set updated_at as a DateTimeField with auto_now set to True to automatically add timestamp on each update
    updated_at = models.DateTimeField(auto_now=True)

    # set string representation of the model to display the size and customer
    def __str__(self):
        return f"<Order {self.size} by {self.customer}"
