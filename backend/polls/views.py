from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Views para API REST
class PollListView(generics.ListAPIView):

    def get_queryset(self):
        from .models import Poll
        return Poll.objects.all()

    def get_serializer_class(self):
        from .serializers import PollSerializer
        return PollSerializer


class PollDetailView(generics.RetrieveAPIView):

    def get_queryset(self):
        from .models import Poll
        return Poll.objects.all()

    def get_serializer_class(self):
        from .serializers import PollSerializer
        return PollSerializer


class VoteCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        from .serializers import VoteSerializer
        return VoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
