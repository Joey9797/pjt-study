from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('and/', views.and_query, name='and_query'),
    path('or/', views.or_query, name='or_query'),
    path('not/', views.not_query, name='not_query'),
    path('compound/', views.compound_query, name='compound_query'),
]
