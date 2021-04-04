from rest_framework import serializers
from .models import Articles

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"

### for showing personal articles of the user
class PostedArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields= ('textArea', 'header', 'image', 'createdAt')