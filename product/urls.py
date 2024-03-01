from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product/<int:pk>/', views.ProductMixin.as_view(), name='product_pg'),
    path('api/products/', views.ProductListAPIView.as_view(), name='product_api'),
    path('api/products/<int:product_id>/lessons/', views.LessonListAPIView.as_view(), name='lesson_api')
]