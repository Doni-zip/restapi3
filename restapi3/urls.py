from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('clients/', ClientListCreateView.as_view(), name="client_endpoint"),
    path('clients/<int:pk>/', ClientRetreiveUpdateDeleteView.as_view(), name="client_detail_endpoint"),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('posts/<int:post_id>/comments/', CommentCreateView.as_view()),
    path('posts/<int:post_id>/like/', LikeCreateView.as_view()),
]