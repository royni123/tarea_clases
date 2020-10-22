from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name='category'),
]