from rest_framework import serializers
from .models import *


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'video_url')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'start_datetime', 'price', 'lessons')


