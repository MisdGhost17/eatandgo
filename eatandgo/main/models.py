from django.db import models
from django.urls import reverse


# Create your models here.


class FoodCard(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="img/")
    display_sostav = models.BooleanField(default=True)
    sostav = models.CharField(max_length=100, default=None, blank=True)
    description = models.TextField(max_length=5000)
    price = models.IntegerField()
    category = models.ForeignKey('FoodCategory', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})