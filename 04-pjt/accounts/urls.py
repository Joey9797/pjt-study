from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('<int:user_pk>/change_password/', views.change_password, name='change_password'),

    path("google/login/", views.google_login, name="google-login"),
    path("google/callback/", views.google_callback, name="google-callback"),

]