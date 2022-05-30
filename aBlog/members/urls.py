from re import template
from django.urls import path

from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views


app_name = 'members' 
# app name to be included in the template url

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    # path("password/", auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path("password/", PasswordsChangeView.as_view()),
    path("password_success", views.password_success, name="password_success"),
    # path("profile_page/", views.profile, name="profile_page"),
    path('<int:pk>/<str:name>/profile/', views.showProfilePageView.as_view(), name="show_profile"),
    path('<int:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name="edit_profile_page"),
    path('<int:pk>/create_profile/', views.CreateProfilePageView.as_view(), name="create_profile")
]