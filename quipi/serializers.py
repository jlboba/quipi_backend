from rest_framework import serializers 
from .models import Prompt
from .models import Quip

class QuipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quip
        fields = ('__all__')

class PromptSerializer(serializers.ModelSerializer):
    quips = QuipSerializer(many=True, read_only=True)

    class Meta:
        model = Prompt
        fields = ('text', 'creator_name', 'accepted', 'quips')
