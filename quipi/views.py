from rest_framework import generics
from .serializers import PromptSerializer
from .serializers import QuipSerializer
from .models import Prompt
from .models import Quip

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

class QuipList(generics.ListCreateAPIView):
    queryset = Quip.objects.all()
    serializer_class = QuipSerializer

class QuipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quip.objects.all()
    serializer_class = QuipSerializer