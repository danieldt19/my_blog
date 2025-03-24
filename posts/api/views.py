from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostViewSet(ViewSet):
    def list(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True) #El many indica que devuelva todos los objetos del array completo del post
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=int):
        post = PostSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=post.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
