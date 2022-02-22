from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .forms import ReviewForm
from .models import Recipe, Tribe, Review


def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    page = request.GET.get('page', 1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, return the first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range, return the last page of results.
        items = paginator.page(paginator.num_pages)
    return items


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
    recipes = Recipe.objects.filter(tribe=tribe)
    recipes = mk_paginator(request, recipes, 2)

    template = 'recipe/tribe.html'
    context = {
        'tribe': tribe,
        'recipes': recipes,
    }

    return render(request, template, context)


def recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    reviews = recipe.reviews.filter(active=True)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.recipe = recipe
            review.save()
            messages.success(request,
                             "Your review was submitted successfully.")
            return redirect(recipe)
    else:
        form = ReviewForm()

    template = 'recipe/detail.html'
    context = {
        'recipe': recipe,
        'form': form,
        'reviews': reviews,
    }

    return render(request, template, context)


def recipe_search(request):
    pass
