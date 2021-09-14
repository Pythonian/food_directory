from django.urls import path

from .views import home, tribe, recipe

app_name = 'recipe'

urlpatterns = [
    path('', home, name='home'),
    path('tribe/<slug:slug>/', tribe, name='tribe'),
    path('recipe/<slug:slug>/', recipe, name='detail'),
]
