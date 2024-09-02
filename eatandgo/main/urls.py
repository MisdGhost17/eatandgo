from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = "main"),
    path('foodcard=<int:pk>', views.FoodCardDetailView.as_view(), name="foodcard_detail"),
    path('new_foodcard', views.create_foodcard, name='add_foodcard'),
    path('update=<int:pk>', views.FoodCardUpdateView.as_view(), name='update_foodcard'),
    path('delete=<int:pk>', views.FoodCardDeleteView.as_view(), name='delete_foodcard'),
    path('category/<int:cat_id>', views.show_category, name='category'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]