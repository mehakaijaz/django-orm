
from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db.models.functions import Upper
from django.db.models import Count,Avg,Min,Max,Sum
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
    one_month_ago=timezone.now() -timezone.timedelta(days=31)
    sales= Sale.objects.filter(datetime__gte=one_month_ago)
    # print(Restaurant.objects.aggregate(Count('id')))
    # print(Rating.objects.aggregate(avg=Avg('rating')))
    # print(Sale.objects.aggregate(min=Min('income'),sum=Sum('income')))
    # print(Sale.objects.aggregate(max=Max('income')))
    print(sales.aggregate(
        min=Min('income'),sum=Sum('income'),max=Max('income')
    ))