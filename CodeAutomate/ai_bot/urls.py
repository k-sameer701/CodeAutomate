from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='user_profile'),
    path('', views.ai_bot, name='ai_bot'),
]