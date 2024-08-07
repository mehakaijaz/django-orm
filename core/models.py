from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

def validate_restaurant_name_begins_with_a(value):
    if not value.startswith('a'):
        raise ValidationError('name of the restaurant doesnt start with a')

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'
    
    name=models.CharField(max_length=100,validators=[validate_restaurant_name_begins_with_a],unique=True)
    website=models.URLField(default='')
    date_opened=models.DateField()
    latitude=models.FloatField(validators=[MinValueValidator(-90),MaxValueValidator(90)])
    longitude=models.FloatField(validators=[MinValueValidator(-180),MaxValueValidator(180)])
    restaurant_type=models.CharField(max_length=2,choices=TypeChoices.choices)
    capacity=models.PositiveSmallIntegerField(null=True,blank=True)
    nickname=models.CharField(max_length=200,null=True,blank=True)
    comments=GenericRelation("Comment")
    
    class Meta:
        ordering=[Lower('name')]
    
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)

class Staff(models.Model):
    name=models.CharField(max_length=128)
    restaurants=models.ManyToManyField(Restaurant,through="StaffRestaurant")
    
    def __str__(self):
        return self.name
    
class StaffRestaurant(models.Model):
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    salary=models.FloatField(null=True)
    
        
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='ratings')
    rating=models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)] #using validators
    )
    comments=GenericRelation("Comment")
    
    def __str__(self):
        return f'Rating : {self.rating}'
    
    class Meta:
        constraints=[
            models.CheckConstraint(
                name='rating value valid',
                check=Q(rating__gte=1,rating__lte=5),
                violation_error_message="Rating invalid: must fall btw 1 and 5"
                
            )
        ]
    
class Sale(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    expenditure = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()
      
class Product(models.Model):
    name=models.CharField(max_length=100)
    num_in_stock=models.PositiveSmallIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    num_of_items= models.PositiveSmallIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.num_of_items} * {self.product.name}' 
    
class Comment(models.Model):
    text=models.TextField()
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveSmallIntegerField()
    content_object=GenericForeignKey("content_type","object_id")