from django.db import models
from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from foods.forms import CreateFoodForm
from .models import Food
from django.contrib.auth.forms import UserCreationForm

# class CreateFoodView(FormView):
#     template_name = 'createfood.html'
#     form_class = CreateFoodForm
#     success_url = '/'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         # form.send_email()
#         # return super().form_valid(form)
#         pass


class FoodCreateView(CreateView):
    model = Food
    fields = ['food_name', 'food_image', 'food_price', 'food_category']
    template_name = 'foods/createfood.html'
    success_url = reverse_lazy('foods')


class FoodUpdateView(UpdateView):
    model = Food
    fields = ['food_name']
    template_name = 'foods/updatefood.html'
    success_url = reverse_lazy('')


class FoodDeleteView(DeleteView):
    model = Food
    success_url = reverse_lazy('')
    template_name = 'foods/deletefood.html'


class FoodShowView(ListView):
    template_name = 'foods/showfood.html'
    model = Food
    context_object_name = 'foods'


