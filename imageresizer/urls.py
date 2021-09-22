from . import views
from django.urls import path

app_name = 'imageresizer'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_image/', views.ImageCreateView.as_view(), name='create_image'),
    path('update_image/<int:pk>', views.ImageUpdateView.as_view(), name='update_image'),
]
