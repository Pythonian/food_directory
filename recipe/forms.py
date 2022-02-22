from django import forms
from django.forms import widgets
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['body']
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Leave a review..."
                }
            )
        }
