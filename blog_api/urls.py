from django.urls import path, include
from blog_api import views

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('post', views.PostViewSet)


urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('users/register/', views.UserRegistrationView.as_view()),
    path('users/logout/', views.CustomLogoutView.as_view()),
    path('users/rest_auth/', include('rest_auth.urls')),

    path('categories/', views.CategoryView.as_view()),

    # path('', include(router.urls)),
    # path('posts/', views.PostListView.as_view()),
    # path('posts/<int:pk>/', views.PostDetailView.as_view()),
    # path('post/create/', views.PostCreateView.as_view()),
    # path('posts/update/<int:pk>/', views.PostUpdateView.as_view()),
    # path('posts/delete/<int:pk>/', views.PostDeleteView.as_view()),

    path('posts/', views.PostView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),



]