from django.urls import path
from . import views

app_name='news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('tag/<slug:tag_slug>/', views.news_list, name='news_list_by_tag'),
    path('<slug:c_slug>/', views.news_detail, name='news_detail')
]
