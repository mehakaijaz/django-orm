#creating modelform that uses model field validators
from django import forms
from core.models import Rating

class RatingForm(forms.ModelForm):
    
    class Meta:
        model=Rating
        fields=('restaurant','rating','user')