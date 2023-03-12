from .models import Order
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):
  size = serializers.CharField(max_length=25)
  order_status = serializers.HiddenField(max_length=25, default=PENDING)
  quantity = serializers.IntegerField()
  created_at = serializers.DateTimeField(auto_now_add=True)
    class Meta:
      model = Order
      fields = ['size', 'order_status', 'quantity']
      
    

    
