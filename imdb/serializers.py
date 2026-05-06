from rest_framework import serializers
from .models import Imdb


class ImdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imdb
        fields = ('product_id', 'code', 'description', 'category', 'brand', 'manufacturer', 'status' )