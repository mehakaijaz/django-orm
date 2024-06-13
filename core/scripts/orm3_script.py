##qs filtering and lookups
from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint 
from django.db.models.functions import Lower


def run():
    """filter down to only one restaurant
    restaurant=Restaurant.objects.filter(name='Pizzaire1')#restaurant_type=Restaurant.TypeChoices.CHINESE)
    restaurant=Restaurant.objects.get(name='Pizzaire1')#restaurant_type=Restaurant.TypeChoices.CHINESE)
    print(restaurant)
    print(restaurant.get())#getting single model back
    #print(connection.queries)
    
    multiple AND conditional with filter()
    
    chinese=Restaurant.TypeChoices.CHINESE
    restaurants=Restaurant.objects.filter(restaurant_type=chinese,name__startswith='C')
    print(restaurants)
    print(connection.queries)
    
    filtering qs with the "in" lookup
    chinese=Restaurant.TypeChoices.CHINESE
    mexican=Restaurant.TypeChoices.MEXICAN
    check_types=[ chinese,mexican]
    restaurant=Restaurant.objects.filter(restaurant_type__in=check_types)
    print(restaurant)
    print(connection.queries)
    
    filtering qs with the exclude()
    chinese=Restaurant.TypeChoices.CHINESE
    indian=Restaurant.TypeChoices.INDIAN
    #restaurant=Restaurant.objects.exclude(restaurant_type=chinese)
    restaurant=Restaurant.objects.exclude(restaurant_type=[chinese,indian])
    print(restaurant)
    print(connection.queries)"""
    
    #lt and gt lookups
    '''rest=Restaurant.objects.filter(name__lt='E')
    rest=Restaurant.objects.filter(longitude__gt=0)
    print(rest)
    pprint(connection.queries)    
    
    #range lookmup
    sales=Sale.objects.filter(income__range=[50,60])
    #rest=Restaurant.objects.filter(longitude__gt=0)
    print([sale.income for sale in sales])
    pprint(connection.queries) '''
    
    #ordering record using orderby()
    """rest=Restaurant.objects.order_by(Lower('name')).reverse()
    print(rest)
    resti=Restaurant.objects.order_by('-name')
    print(resti)# both d print statements gives same result
    pprint(connection.queries)"""
    # ordering is case sensitive lowercase is added at last
    
     #ordering record using datetime fields
    """resti=Restaurant.objects.order_by('date_opened')
    print(resti)
    restie=Restaurant.objects.order_by('date_opened')[0]#indexing
    print(restie)
    restie=Restaurant.objects.order_by('date_opened')[:6]#slicing
    print(restie)
    restiey=Restaurant.objects.order_by('date_opened')[2:6]# particular slicing me offset hota hai
    print(restiey)
    pprint(connection.queries)"""
     
     