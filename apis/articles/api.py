from rest_framework import viewsets,permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Articles
from .serializers import ArticleSerializer

class ArticleViewset(viewsets.ModelViewSet):

    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


## All Recent Articles
class RecentArticles(viewsets.ModelViewSet):

    serializer_class = ArticleSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        return Articles.objects.order_by('-id')[:3]


## Personal Articles
class PersonalArticles(viewsets.ModelViewSet):
    
    serializer_class = ArticleSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return self.request.user.articles.all()

