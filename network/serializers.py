from rest_framework import serializers
from .models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер модели продукта."""
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Узла сети."""
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkNode
        exclude = ['debt_to_supplier']  # Запрет на обновление этого поля через API


class NetworkNodeListSerializer(serializers.ModelSerializer):
    """Сериалайзер модели списка Узлов сетей."""
    class Meta:
        model = NetworkNode
        fields = '__all__'
