from django.views.generic import TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from rest_framework import generics
from .serializers import *


class IndexView(TemplateView):
    template_name = 'product/index.html'


# Проерка того,авторизован ли пользователь для доступа к продукту.
class ProductMixin(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Product
    login_url = 'login_page'
    template_name = 'product/products.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.Group.group_members.filter(pk=self.request.user.pk).exists():
            raise PermissionError
        return obj

    def handle_no_permission(self):
        return HttpResponseForbidden('Необходима авторизация для получения доступа!')


# API на список продуктов
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# API с выведением списка уроков по конкретному продукту
class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(product_id=product_id)