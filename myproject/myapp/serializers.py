from rest_framework import serializers
from .models import Student , Image_Gallery , Videos_Gallery, Blog, Events ,Message , Ranking 
from django.contrib.auth.hashers import make_password

class studentsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class imagesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Image_Gallery
        fields = '__all__'

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos_Gallery
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


# class GameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = '__all__'