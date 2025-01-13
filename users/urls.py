from django.urls import path
from .views import login, register, logout, user_account, user_update


urlpatterns = [
    path('login/', login, name='user-login'),
    path('register/', register, name='user-register'),
    path('logout/', logout, name='user-logout'),
    path('<str:username>/', user_account, name='user-account'),
    path('update/<str:username>/', user_update, name='user-update'),
]