from django.urls import path
from .views import PostsPageView

urlpatterns = [
    path('posts/', PostsPageView.as_view(), name='posts'),
]
