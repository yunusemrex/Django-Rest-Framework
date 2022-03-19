from rest_framework.generics import CreateAPIView
from comment.api.serializers import CommentCreateSerializer
from comment.models import Comment
from rest_framework.permissions import IsAuthenticated


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer 
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

