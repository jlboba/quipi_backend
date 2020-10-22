from rest_framework import serializers 
from .models import Prompt
from .models import Quip

class PromptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prompt
        fields = ('id', 'text', 'creator_name', 'accepted',)

class QuipSerializer(serializers.HyperlinkedModelSerializer):
    prompt_url = serializers.HyperlinkedIdentityField(view_name="prompt_detail")

    class Meta:
        model = Quip
        fields = ('id', 'prompt_url','text', 'times_played', 'times_chosen', 'creator_name', 'accepted')