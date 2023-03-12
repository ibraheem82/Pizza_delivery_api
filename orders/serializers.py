from .models import Order
from rest_framework import serializers
import datetime

class OrderCreationSerializer(serializers.ModelSerializer):
  size = serializers.CharField(max_length=25)
  order_status = serializers.HiddenField(default='PENDING')
  quantity = serializers.IntegerField()
  created_at = serializers.DateTimeField(default=serializers.CreateOnlyDefault(datetime.datetime.now))


  class Meta:
    model = Order
      fields = ['size', 'order_status', 'quantity']
      
    

    
