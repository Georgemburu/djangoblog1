from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostEditView,
    PostDeleteView,
)


urlpatterns = [
     path('', PostListView.as_view()),
     path('post/<int:pk>/', PostDetailView.as_view()),
     path('post/create/',PostCreateView.as_view()),
     path('post/<int:pk>/edit',PostEditView.as_view()),
     path('post/<int:pk>/delete',PostDeleteView.as_view())
]
