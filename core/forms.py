#creating modelform that uses model field validators
from django import forms
from core.models import Rating,Restaurant,Order
from django.core.validators import MinValueValidator,MaxValueValidator

# class RatingForm(forms.ModelForm):
    
    # class Meta:
    #     model=Rating
    #     fields=('restaurant','rating','user')
    
class RatingForm(forms.Form):
    rating=forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
class RestaurantForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields=('name','restaurant_type')

class ProductStockException(Exception):
    pass

class ProductOrderForm(forms.ModelForm):
    
    class Meta:
        model=Order
        fields=('product','num_of_items')
        
    def save(self):
        order=super().save(commit=False)
        if order.product.num_in_stock < order.num_of_items:
            raise ProductStockException(
                f" not enough items in stock: {order.product}"
            )
        if commit:
            order.save()
        return order