from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter 

urlpatterns = [
    path('prompts', views.PromptList.as_view(), name='prompt_list'),
    path('prompts/<int:pk>', views.PromptDetail.as_view(), name='prompt_detail'),
    path('quips', views.QuipList.as_view(), name='quip_list'),
]