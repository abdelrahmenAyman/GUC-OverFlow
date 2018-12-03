from django.urls import path, include

from rest_framework.routers import DefaultRouter

from polls import views


router = DefaultRouter()
router.register('polls', views.PollsView, basename='poll')

urlpatterns = [
    path('', include(router.urls))
]
