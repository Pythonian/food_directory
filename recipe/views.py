from django.shortcuts import render, get_object_or_404

from .models import Recipe, Tribe


def home(request):
    tribes = Tribe.objects.all()
    featured_recipes = Recipe.objects.all()[:3]

    template = 'recipe/home.html'
    context = {
        'tribes': tribes,
        'featured_recipes': featured_recipes,
    }

    return render(request, template, context)


def tribe(request, slug):
    tribe = get_object_or_404(Tribe, slug=slug)

    template = 'recipe/tribe.html'
    context = {
        'tribe': tribe,
    }

    return render(request, template, context)


def recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    template = 'recipe/detail.html'
    context = {
        'recipe': recipe,
    }

    return render(request, template, context)
