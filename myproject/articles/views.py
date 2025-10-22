from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthorOrReadOnly

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthorOrReadOnly])
    def publish(self, request, pk=None):
        article = self.get_object()
        self.check_object_permissions(request, article)

        if article.published:
            return Response({'detail': 'Already published'}, status=status.HTTP_400_BAD_REQUEST)

        article.published = True
        article.save()
        serializer = self.get_serializer(article)
        return Response(serializer.data)
