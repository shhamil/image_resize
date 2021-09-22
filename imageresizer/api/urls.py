from django.urls import path
from .api_views import PikchaListApiView, PikchaDetailView, PikchaResizeView

urlpatterns = [
    path('images/', PikchaListApiView.as_view(), name='api_images'),
    path('images/<int:pk>/', PikchaDetailView.as_view(), name='api_images_detail'),
    path('images/<int:pk>/resize/', PikchaResizeView.as_view(), name='api_images_resize'),
]
