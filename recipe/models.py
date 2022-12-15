from django.conf import settings
from django.db import models
from django.urls import reverse


class Tribe(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe:tribe', kwargs={'slug': self.slug})


class Recipe(models.Model):
    BREAKFAST = 'B'
    LUNCH = 'L'
    DINNER = 'D'
    MEAL_PERIOD_CHOICES = (
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)
    description = models.TextField()
    cooking_time = models.CharField(max_length=20)
    preparation_time = models.CharField(max_length=20)
    meal_period = models.CharField(
        max_length=10,
        choices=MEAL_PERIOD_CHOICES)
    servings = models.PositiveIntegerField()
    image = models.ImageField(upload_to='recipes')
    image_caption = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'

    def get_previous_recipe(self):
        return self.get_previous_by_created()

    def get_next_recipe(self):
        return self.get_next_by_created()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe:detail', kwargs={'slug': self.slug})


class Preparation(models.Model):
    text = models.TextField()
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='preparations')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='ingredients')
    image = models.ImageField(upload_to='ingredients')
    text = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    body = models.CharField('Your Review', max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Review by {self.author} on {self.recipe}"


class CookingTool(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='tools')
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
