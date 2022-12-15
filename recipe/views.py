from django.contrib import messages
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render, get_object_or_404

from .forms import ReviewForm
from .models import Recipe, Tribe


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
    trending_recipes = Recipe.objects.order_by("?")[:3]
    latest_recipes = Recipe.objects.order_by("-created")[:5]
    featured_recipes = Recipe.objects.filter(featured=True)

    template = 'recipe/home.html'
    context = {
        'tribes': tribes,
        'featured_recipes': featured_recipes,
        'trending_recipes': trending_recipes,
        'latest_recipes': latest_recipes,
    }

    return render(request, template, context)


def tribe(request, slug):
    tribe = get_object_or_404(Tribe, slug=slug)
    recipes = Recipe.objects.filter(tribe=tribe)
    recipes = mk_paginator(request, recipes, 10)

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


def search(request):
    q = request.GET.get('q', None)
    recipes = ''
    if q is None or q == "":
        recipes = Recipe.objects.all()
    elif q is not None:
        recipes = Recipe.objects.filter(
            Q(name__icontains=q) | Q(description__icontains=q)).distinct()
    return render(request, 'recipe/search.html', {'recipes': recipes})
