from django.urls import path

from polls import views

urlpatterns = [
    path('polls', views.PollsView.as_view(), name='polls')
]
