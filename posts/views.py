from rest_framework import permsissions, viewsets
from rest_framework.response import Response

from posts.models import Post
from posts.permsissions import IsAuthorOfPost
from posts.serializers import PostSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (persmissions.AllowAny(),)
        return (persmissions.IsAuthenticated(), IsAuthorOfPost(),)
    
    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)
        
        return super(PostViewSet, self).perform_create(serializer)
        
class AccountPostsViewSet(viewsets.Viewset):
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer
    
    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)
        
        return Response(serializer.data)