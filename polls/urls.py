from django.urls import path, include

from rest_framework.routers import DefaultRouter

from polls import views


router = DefaultRouter()
router.register('', views.PollsView)

urlpatterns = [
    path('', include(router.urls)),
    path('polls', views.PollsView.as_view(), name='polls')
]
