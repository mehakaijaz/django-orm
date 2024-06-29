
from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db.models.functions import Upper,Length,Concat,Coalesce
from django.db.models import Count,Avg,Min,Max,Sum
from django.db.models import F,Q
from django.db import connection
from pprint import pprint 
import random

def run():
    '''rating=Rating.objects.first()
    print(rating.rating)
    
    #update this rating
    #rating.rating+=1
    rating.rating=F('rating')+1
    rating.save()
    rating.refresh_from_db()
    print(rating.rating)#type = combined expressions
     
    # Rating.objects.update(rating=F('rating')*2)
    sales= Sale.objects.all()
    for sale in sales:
        sale.expenditure= random.uniform(5,100)
    
    Sale.objects.bulk_update(sales,['expenditure'])
    
    sales= Sale.objects.filter(expenditure__gt=F('income'))
    sales=Sale.objects.annotate(
        profit=F('income')-F('expenditure')
    ).order_by('-profit')
    
    print(sales.first().profit)
    sales=Sale.objects.aggregate(
        profit=Count('id',filter=Q(income__gt=F('expenditure'))),
        loss=Count('id',filter=Q(income__lt=F('expenditure')))
    )  
    print(sales)
    
    #pprint(connection.queries)'''
    
    """ #get all it or mx rests
    it=Restaurant.TypeChoices.ITALIAN
    mx=Restaurant.TypeChoices.MEXICAN
    r=Restaurant.objects.filter(
        Q(restaurant_type=it)| Q(restaurant_type=mx) ) 
    print(r)
    
    #find any rest that have the num 1 in the name
    r=Restaurant.objects.filter(name__icontains="1")
    print(r)
    ri=Restaurant.objects.filter(name__endswith="1")
    print(ri)
    
    #rest name contains either it or mx
    rs=Restaurant.objects.filter(
        Q(name__icontains='italian')|Q(name__icontains='mexican'))
    for r in rs:
        print(r.name)
    it_or_mx=Q(name__icontains='italian')|Q(name__icontains='mexican')
    not_recently_opened=~Q(date_opened=timezone.now()-timezone.timedelta(days=40))
    rs=Restaurant.objects.filter(it_or_mx|not_recently_opened)
    
    print(rs)"""
    
    #we want to find all sales where:
    # -profit is greater than expenditure
    # -rest name conatins a num
    
    """name_has_num=Q(restaurant__name__regex=r"[0-9]+")
    profit=Q(income__gt=F('expenditure'))
    s1=Sale.objects.filter(name_has_num & profit)#.values_list("restaurant__name",flat=True)
    s2=Sale.objects.filter(name_has_num | profit)
    print(s1.count(), s2.count())
    
    # for sale in s:
    #     if sale.income <= sale.expenditure:
    #         print(sale.restaurant.name)"""
    """rest1=Restaurant.objects.first()
    rest2=Restaurant.objects.last()
    rest1.capacity=100
    rest2.capacity=200
    rest1.save()
    rest2.save()
    print(
        Restaurant.objects.filter(capacity__isnull=False).count()
    )"""
    #pprint(connection.queries)
    
    '''print(
        Restaurant.objects.order_by(F('capacity').asc(nulls_last=True)).values('capacity'))
    print(
        Restaurant.objects.filter(capacity__isnull=False).order_by('-capacity').values('capacity'))'''
    #coalesce functions
    #Restaurant.objects.update(capacity=None)
    '''print(Restaurant.objects.aggregate(total_cap=Coalesce(Sum('capacity'),0)))
    print(Rating.objects.filter(rating__lt=0).aggregate(total=Avg('rating',default=0)))
    pprint(connection.queries)'''
    
    r=Restaurant.objects.last()
    r.nickname="efgh"
    r.save()
    print(Restaurant.objects.annotate(
        name_value=Coalesce(F('nickname'),F('name'))
    ).values('name_value'))
    