from django.db import models
from django.urls import reverse


class Tribe(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tribe:detail', kwargs={'slug': self.slug})


class Recipe(models.Model):
    BREAKFAST = 'B'
    LUNCH = 'L'
    DINNER = 'D'
    MEAL_PERIOD_CHOICES = (
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    )
    NATIVE = 'N'
    POPULAR = 'P'
    FOOD_CLASS_CHOICES = (
        (NATIVE, 'Native'),
        (POPULAR, 'Popular'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)
    meal_period = models.CharField(
        max_length=1,
        choices=MEAL_PERIOD_CHOICES)
    food_class = models.CharField(
        max_length=1,
        choices=FOOD_CLASS_CHOICES)
    image = models.ImageField(upload_to='recipes')
    image_caption = models.CharField(max_length=100)
    video = models.URLField(blank=True)
    ingredients = models.TextField()
    preparation = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe:detail', kwargs={'slug': self.slug})
