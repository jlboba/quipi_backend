from rest_framework import generics
from .serializers import PromptSerializer
from .serializers import QuipSerializer
from .models import Prompt
from .models import Quip

class PromptList(generics.ListCreateAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

class PromptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

class QuipList(generics.ListCreateAPIView):
    queryset = Quip.objects.all()
    serializer_class = QuipSerializer