# system/api/serializers.py
from rest_framework import serializers
from .models import Product, Sale, SaleItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock", "created_at"]
        read_only_fields = ["created_at"]


class SaleItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )

    class Meta:
        model = SaleItem
        fields = ["product_id", "product_name", "quantity", "unit_price"]
        read_only_fields = ["unit_price", "product_name"]


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True, read_only=True)

    create_items = serializers.ListField(
        child=serializers.DictField(
            child=serializers.IntegerField(),
        ),
        write_only=True,
    )

    class Meta:
        model = Sale
        fields = ["id", "date", "items", "create_items"]
        read_only_fields = ["date"]
