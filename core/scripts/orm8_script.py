from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db.models.functions import Upper,Length,Concat,Coalesce
from django.db.models import OuterRef,Subquery,Exists
from django.db.models import F,Q,Value,CharField
from django.db import connection
from pprint import pprint 
import random
import itertools
def run():
    '''s=Sale.objects.filter(restaurant__restaurant_type__in=['IT','CH'])
    print(len(s))
    print(s.values_list('restaurant__restaurant_type').distinct())
    rest=Restaurant.objects.filter(restaurant_type__in=['IT','CH'])
    sales=Sale.objects.filter(restaurant__in=Subquery(rest.values('pk')))
    print(len(sales))'''
    
    """rest=Restaurant.objects.all()
    sales=Sale.objects.filter(restaurant=OuterRef('pk')).order_by('-datetime')
    rest=rest.annotate(
        last_sale_income=Subquery(sales.values('income')[:1]),
        last_sale_expenditure=Subquery(sales.values('expenditure')[:1]),
        profit=F('last_sale_income') - F('last_sale_expenditure'),
    )
    for r in rest:
        print(f"{r.pk} - {r.last_sale_income}")"""
        
    '''rest=Restaurant.objects.filter(
        #Exists(Sale.objects.filter(restaurant=OuterRef('pk'),income__gt=5)),
        ~Exists(Rating.objects.filter(restaurant=OuterRef('pk'),rating=4))
    )
    print(rest.count())'''
    
    five_days_ago=timezone.now() - timezone.timedelta(days=10)
    sales=Sale.objects.filter(restaurant=OuterRef('pk'),datetime__lte=five_days_ago)
    rest=Restaurant.objects.filter(Exists(sales))
    print(rest.count())