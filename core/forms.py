#creating modelform that uses model field validators
from django import forms
from core.models import Rating,Restaurant


# class RatingForm(forms.ModelForm):
    
    # class Meta:
    #     model=Rating
    #     fields=('restaurant','rating','user')
    
    
from django.core.validators import MinValueValidator,MaxValueValidator

class RatingForm(forms.Form):
    rating=forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
class RestaurantForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields=('name','restaurant_type')