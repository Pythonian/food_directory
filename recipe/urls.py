from django.urls import path

from .views import home, tribe, recipe, search

app_name = 'recipe'

urlpatterns = [
    path('search/', search, name='search'),
    path('tribe/<slug:slug>/', tribe, name='tribe'),
    path('recipe/<slug:slug>/', recipe, name='detail'),
    path('', home, name='home'),
]
