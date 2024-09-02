import os

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import FoodCardForm

from .models import FoodCard, FoodCategory

# Create your views here.
def main(request):
    foodcards = FoodCard.objects.all()
    categories = FoodCategory.objects.all()
    data = {
        'title': 'Главная страница',
        'foodcards': foodcards,
        'categories':categories,
        'cat_selected': 0,
    }
    return render(request, "main/index.html", data)

def contact(request):
    return render(request, "main/contact.html")

def about(request):
    return render(request, "main/about.html")

class FoodCardDetailView(DetailView):
    model = FoodCard
    context_object_name = 'foodcard'
    template_name = 'main/foodcard_detail.html'

def create_foodcard(request):
    if request.method == 'POST':
        form = FoodCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main")
    form = FoodCardForm()

    data = {
        'form': form,
    }
    return render(request,'main/new_foodcard.html', data)

class FoodCardUpdateView(UpdateView):
    model = FoodCard
    template_name = 'main/new_foodcard.html'
    form_class = FoodCardForm

    success_url = "/"

class FoodCardDeleteView(DeleteView):
    model = FoodCard
    success_url = '/'


def show_category(request, cat_id):
    foodcards = FoodCard.objects.filter(category=cat_id)
    categories = FoodCategory.objects.all()

    if len(foodcards) == 0:
        raise Http404()
    data = {
        'title': 'Главная страница',
        'foodcards': foodcards,
        'categories': categories,
        'cat_selected': cat_id,
    }
    return render(request, "main/index.html", data)


