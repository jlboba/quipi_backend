from rest_framework import serializers 
from .models import Prompt
from .models import Quip

class QuipSerializer(serializers.ModelSerializer):
    prompt = serializers.StringRelatedField(many=False)

    class Meta:
        model = Quip
        fields = ('prompt', 'prompt_id', 'text', 'times_played', 'times_chosen', 'creator_name', 'accepted')

class PromptSerializer(serializers.ModelSerializer):
    quips = QuipSerializer(many=True, read_only=True)

    class Meta:
        model = Prompt
        fields = ('text', 'creator_name', 'accepted', 'quips')
