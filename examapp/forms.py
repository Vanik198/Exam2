from django import forms
from .models import Course

class RatingForm(forms.Form):
    rating = forms.FloatField(min_value=0, max_value=5, required=True, label="Your Rating")