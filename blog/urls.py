from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.AllBlog.as_view(), name='all_blogs'),
    path('<int:pk>', views.OneBlog.as_view(), name='one_blog'),
]
