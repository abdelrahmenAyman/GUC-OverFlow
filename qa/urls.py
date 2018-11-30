from django.urls import path, include

from rest_framework import routers

from qa import views

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
]
