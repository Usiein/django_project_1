from django.urls import path
from .views import BlogPostPageView, BlogDetailView

urlpatterns = [
    path('blog/', BlogPostPageView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
