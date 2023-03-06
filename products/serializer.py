from rest_framework import serializers
from .models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','description']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    catetory_name = serializers.CharField(source = 'category.name',read_only=True)
    catetory_description = serializers.CharField(source = 'category.description',read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        fields.__add__('catetory_name')
        fields.__add__('catetory_description')

