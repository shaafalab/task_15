from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
        	'name',
        	'opening_time',
        	'closing_time',
        	]

class RestaurantDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
        	'id',
        	'owner',
        	'description',
        	'name',
        	'opening_time',
        	'closing_time',
        	]        	

class RestaurantListupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
        	'description',
        	'name',
        	'opening_time',
        	'closing_time',
        	]