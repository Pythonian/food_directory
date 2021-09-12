from django.contrib import admin
from .models import Recipe, Tribe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'tribe', 'meal_period']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    date_hierarchy = 'created'
    list_filter = ['tribe__name', 'food_class', 'meal_period']


@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ['name']
