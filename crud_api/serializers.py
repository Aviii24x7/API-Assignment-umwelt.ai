from rest_framework import serializers
from .models import Category, Product, Order


# serialiser for models
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    # Doing Validations
    def validate(self, data):
        if data['quantity'] > 0:
            data['is_available'] = True
        else:
            data['is_available'] = False
        
        return data
    
    
class OrderSerializer(serializers.ModelSerializer):
    
    # products = ProductSerializer(many=True)
    
    class Meta:
        model = Order
        fields = '__all__'
        
    
# automatically calculating price from product model irrespective of order model
    def validate(self, data):
        final_price =0
        
        for i in data['products']:
            final_price += i.price
        
        data['total_price'] = final_price
            
        return data
