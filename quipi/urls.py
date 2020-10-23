from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter 

urlpatterns = [
    path('prompts/', views.PromptList.as_view(), name='prompt_list'),
    path('prompts?playable=<playable>', views.PromptList.as_view(), name='prompt_list'),
    path('prompts/<int:pk>', views.PromptDetail.as_view(), name='prompt_detail'),
    path('quips/', views.QuipList.as_view(), name='quip_list'),
    path('quips?playable=<playable>', views.QuipList.as_view(), name='quip_list'),
    path('quips/<int:pk>', views.QuipDetail.as_view(), name='quip_detail'),
]