from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        #fields = '__al__'
        fields = ('title', 'description', 'order', 'created_at')
