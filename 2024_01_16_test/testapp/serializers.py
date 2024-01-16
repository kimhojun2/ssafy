from rest_framework import serializers
from .models import Post, Comment

# class CommentSerializer(serializers.ModelSerializer):
#     class Post


class CommentSerializer(serializers.ModelSerializer):
    class PostTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('title',)
    
    post = PostTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'