from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.mail import send_mass_mail
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

    def save_model(self, request, obj, form, change):
        all_users = get_user_model().objects.all()
        subject = 'New recipe created.'
        message = 'A new recipe has just been created on our website.'
        data = [
            (subject, message, "admin@foodrecipe.com", [user.email])
            for user in all_users
        ]
        send_mass_mail(data)
        super().save_model(request, obj, form, change)


@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
