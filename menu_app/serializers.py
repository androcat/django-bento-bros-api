from django.db.models import fields
from rest_framework import serializers
from .models import Appetizer, MainCourse, Dessert
 
class AppetizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appetizer
        fields = '__all__'

class MainCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCourse
        fields = '__all__'

class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = '__all__'