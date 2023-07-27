from rest_framework import serializers
from .models import Product, Category
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_instance = Category.objects.create(**category_data)
        product_instance = Product.objects.create(category=category_instance, **validated_data)
        return product_instance
    
    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        category_instance = instance.category

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)

        category_instance.gender = category_data.get('gender', category_instance.gender)
        category_instance.colors = category_data.get('colors', category_instance.colors)
        category_instance.save()

        instance.save()
        return instance
