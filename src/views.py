from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response({
            "success": True,
            "message": "Post retrieved successfully",
            "count": posts.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Post created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "message": "Post creation failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
