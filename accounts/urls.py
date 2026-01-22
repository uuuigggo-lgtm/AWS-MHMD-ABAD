from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, logout_view
from .views import user_list, deactivate_user, delete_user,activate_user
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('users/', user_list, name='user_list'),
    path('users/activate/<int:user_id>/', activate_user, name='activate_user'),
    path('users/deactivate/<int:user_id>/', deactivate_user, name='deactivate_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
]