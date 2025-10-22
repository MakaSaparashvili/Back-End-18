from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'content',
            'author', 'author_username',
            'published', 'created_at', 'updated_at'
        ]
        read_only_fields = ['author', 'author_username', 'published', 'created_at', 'updated_at']
