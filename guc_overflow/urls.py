from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('rest_framework.urls')),
    path('accounts/', include('users.urls')),
    path('', include('qa.urls')),
    path('', include('polls.urls'))
]
