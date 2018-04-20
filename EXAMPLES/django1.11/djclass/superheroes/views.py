from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, DetailView, UpdateView
)
from django.shortcuts import render
from .models import Superhero

def home(request):
    data = {
        'message': 'Welcome to the superheroes app for class-based views',
    }
    return render(request, 'home.html', data)


class GenericContext(TemplateView):
    message = 'with context'
    fruits = ['apple', 'banana', 'lemon']
    template_name ='generic_context.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'message': self.message,
                'fruits': self.fruits
            }
        )
        return context


class HeroListViewMinimal(ListView):
    model = Superhero


class HeroDetailViewMinimal(DetailView):
    model = Superhero


class HeroListView(ListView):
    context_object_name = 'heroes'
    template_name = 'hero_list.html'
    model = Superhero


class HeroDetailView(DetailView):
    context_object_name = 'hero'
    template_name = 'superhero_details.html'
    model = Superhero

class HeroCreateView(CreateView):
    model = Superhero
    template = "superhero_create.html"
    fields = ['name', 'real_name', 'secret_identity', 'city']

class HeroUpdateView(UpdateView):
    model = Superhero
    template = "hero_update.html"
    fields = ['name', 'real_name', 'secret_identity', 'city']

