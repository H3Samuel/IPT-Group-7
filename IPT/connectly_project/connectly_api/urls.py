from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

# Create router and register our viewsets
router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),  # This includes /contacts/
]

from django.urls import path
from .views import NewsFeedView

urlpatterns = [
    path('news-feed/', NewsFeedView.as_view(), name='news-feed'),
]
