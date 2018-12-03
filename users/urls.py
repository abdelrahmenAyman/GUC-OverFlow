from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users import views


router = DefaultRouter()
router.register('', views.GucianViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('change-password', views.ChangePasswordView.as_view(),
         name='change-password'),
    path('forget-password', views.ForgetPasswordView.as_view(),
         name='forget-password'),
    path('reset-password/<int:pk>', views.ResetPasswordView.as_view(),
         name='reset-password')
]
