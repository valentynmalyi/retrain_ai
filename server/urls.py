from django.urls import path, include

from issue.urls import urlpatterns

urlpatterns = [
    path('', include(urlpatterns)),
]
