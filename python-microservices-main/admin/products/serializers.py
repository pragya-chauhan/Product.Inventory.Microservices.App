from rest_framework import serializers

from .models import Product

#extending from serializers (imported above) to modelserializer
#inside another class meta and give what is model in our case Product then specify fields
#no serializer for user
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
