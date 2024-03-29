# Generated by Django 4.0.6 on 2022-12-15 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_review_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'get_latest_by': 'created', 'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='recipe',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
