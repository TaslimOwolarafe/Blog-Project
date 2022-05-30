from django.urls import path

# from aBlog.theBlog.models import Category
# from . import views
from theBlog import views
from . views import AddPostView, ArticleDetailView, HomeView, UpdatePostView, DeletePostView, AddCategoryView


app_name = 'theBlog' 
# app name to be included in the template url

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="edit_post"),
    path("article/<int:pk>/remove", DeletePostView.as_view(), name="delete_post"),
    path("category/<str:cat>/", views.CategoryView,name='category'),
    path("category/", views.CategoryListView,name='categories-list'),
    path('like/<int:pk>', views.LikeView, name="like_post"),
    # path('unlike/<int:pk>', views.UnlikeView, name="unlike_post"),

]
