# Generated by Django 3.2.7 on 2022-02-22 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_recipe_preparation_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preparations', to='recipe.recipe')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
