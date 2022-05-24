from rest_framework import serializers
from apps.product.models import Products


# class CategorySerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=150, min_length=5)
#     slug = serializers.SlugField(max_length=150)
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
