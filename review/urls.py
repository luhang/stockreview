from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('create/', views.create_review, name='review_create'),
    path('<int:pk>/', views.review_detail, name='review_detail'),
]
