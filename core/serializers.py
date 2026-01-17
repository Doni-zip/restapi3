from rest_framework import serializers
from datetime import date
from .models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def validate_birth_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Дата рождения не может быть в будущем")
        
        return value
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "text", "created_at"]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "post", "created_at"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at", "comments", "likes_count"]

    def get_likes_count(self, obj):
        return obj.likes.count()
