from django.urls import path

from users import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('change-password', views.ChangePasswordView.as_view(),
         name='change-password')
]
