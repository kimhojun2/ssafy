from rest_framework import serializers
from .models import Post, Comment

# class CommentSerializer(serializers.ModelSerializer):
#     class Post


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'parent_comment',)



class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'