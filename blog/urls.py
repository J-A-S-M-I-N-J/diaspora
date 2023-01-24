from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='blog_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('add', views.add_item, name='add'),
    path('edit/<slug:slug>/', views.edit_item, name='edit'),
    path('toggle/<slug:slug>/', views.toggle_item, name='toggle'),
    path('deletecheck/<slug:slug>/', views.delete_item_view, name='deletecheck'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('postlist', views.PostList.as_view(), name='PostList'),
]
