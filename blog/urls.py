from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(),name='post_list'),
    path('about/', views.AboutView.as_view(),name='about'),
    path(r'post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path(r'post/new/',views.CreatePostView.as_view(),name='post_new'),
    path(r'post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    path(r'post/<int:pk>/remove/',views.PostDeleteView.as_view(),name='post_remove'),
    path('post/drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path(r'post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path(r'post/<int:pk>/approve/comment/',views.comment_approve,name='comment_approve'),
    path(r'post/<int:pk>/remove/comment/',views.comment_remove,name='comment_remove'),
    path(r'post/<int:pk>/publish/',views.post_publish,name='post_publish'),
]
