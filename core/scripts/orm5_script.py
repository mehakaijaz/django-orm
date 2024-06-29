
from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db.models.functions import Upper,Length,Concat
from django.db.models import Count,Avg,Min,Max,Sum
from django.db.models import   CharField,Value,     Variance
from django.db import connection
from pprint import pprint 
import random

def run():
    # rest=Restaurant.objects.values('name','date_opened').first()
    # print(rest)
    # resti=Restaurant.objects.values('name','date_opened').first()
    # print(resti['name'])
    # rest=Restaurant.objects.values('name','date_opened')
    # print(rest)
#    """ rest=Restaurant.objects.values(name_upper=Upper('name'))[:3]
#     print(rest)
# IT = Restaurant.TypeChoices.ITALIAN
# ratings=Rating.objects.filter(restaurant__restaurant_type=IT).values('rating','restaurant__name')
# print(ratings)
# print(connection.queries)"""

    # rest=Restaurant.objects.values_list('name',flat=True)
    # print(rest)
    
    # print(Restaurant.objects.filter(name__startswith='c').count())
    # one_month_ago=timezone.now() -timezone.timedelta(days=31)
    # sales= Sale.objects.filter(datetime__gte=one_month_ago)
    # print(Restaurant.objects.aggregate(Count('id')))
    # print(Rating.objects.aggregate(avg=Avg('rating')))
    # print(Sale.objects.aggregate(min=Min('income'),sum=Sum('income')))
    # print(Sale.objects.aggregate(max=Max('income')))
    # print(sales.aggregate(
    #     min=Min('income'),sum=Sum('income'),max=Max('income')
    # ))
    
    #fetch all rest and assume we want 
    #to get the no of characters in the name of rest.so 'xyz==3'
    # rest=Restaurant.objects.annotate(len_name=Length('name'))
    # resti=Restaurant.objects.annotate(len_name=Length('name')).filter(len_name__gt=10)
    # print(rest.first().len_name)
    # print(rest.values('len_name','name'))
    # print(resti.first().len_name)
    # print(resti.values('len_name','name'))
    
    #rest1 [rating:4.3] we have to get something like this
    # concatenation=Concat('name',Value(' [rating: '),Avg('ratings__rating'),Value(']'),
    #                      output_field=CharField())
    
    # rest=Restaurant.objects.annotate(message=concatenation)
    # for r in rest:
        # print(r.message)  
    
    # rest=Restaurant.objects.annotate(total_sales=Sum('sales__income'))
    # print([r.total_sales for r in rest])   
    # rest=Restaurant.objects.annotate(num_ratings=Count('ratings'),avg_ratings=Avg('ratings'))
    # print(rest.values('name','num_ratings','avg_ratings'))
    
    rest=Restaurant.objects.values('restaurant_type').annotate(num_ratings=Count('ratings'))
    print(rest)