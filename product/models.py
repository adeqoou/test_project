from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    authors = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_datetime = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Автор/Создатель:{self.authors}'


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    min_size = models.PositiveIntegerField(default=1)
    max_size = models.PositiveIntegerField(default=12)


class Group(models.Model):
    name = models.CharField(max_length=255)
    group_members = models.ManyToManyField(to=User)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'Название группы:{self.name}'


class Members(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, null=True, blank=True)