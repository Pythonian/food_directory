from django.contrib import admin
from .models import Recipe, Tribe, Ingredient, CookingTool, Preparation


class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1


class CookingToolInline(admin.StackedInline):
    model = CookingTool
    extra = 1


class PreparationInline(admin.StackedInline):
    model = Preparation
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'tribe', 'meal_period']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    date_hierarchy = 'created'
    list_filter = ['tribe__name', 'meal_period']
    inlines = [IngredientInline, CookingToolInline, PreparationInline]


@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
