from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import PromptSerializer, QuipSerializer
from .models import Prompt, Quip

class PromptList(generics.ListCreateAPIView):
    serializer_class = PromptSerializer

    def get_queryset(self):
        queryset = Prompt.objects.all()
        playable = self.request.query_params.get('playable', None)
        if playable is not None:
            if playable == 'true' or playable == 't':
                accepted = True 
            elif playable == 'false' or playable == 'f':
                accepted = False 
            else:
                accepted = True 
            queryset = queryset.filter(accepted=accepted)
        return queryset

class PromptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'DELETE':
            return [permission() for permission in self.permission_classes]
        return [AllowAny()]


class QuipList(generics.ListCreateAPIView):
    queryset = Quip.objects.all()
    serializer_class = QuipSerializer

    def get_queryset(self):
        queryset = Quip.objects.all()
        playable = self.request.query_params.get('playable', None)
        if playable is not None:
            if playable == 'true' or playable == 't':
                accepted = True 
            elif playable == 'false' or playable == 'f':
                accepted = False 
            else:
                accepted = True 
            queryset = queryset.filter(accepted=accepted)
        return queryset

class QuipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quip.objects.all()
    serializer_class = QuipSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'DELETE':
            return [permission() for permission in self.permission_classes]
        return [AllowAny()]