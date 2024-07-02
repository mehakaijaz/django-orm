from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db.models.functions import Upper,Length,Concat,Coalesce
from django.db.models import Count,Avg,Min,Max,Sum,Case,When
from django.db.models import F,Q,Value,CharField
from django.db import connection
from pprint import pprint 
import random
import itertools
def run():
    it=Restaurant.TypeChoices.ITALIAN
    
    '''rs=Restaurant.objects.annotate(
        is_it=Case(
            When(restaurant_type=it,then=True),default=False)
        )
    print(
        rs.filter(is_it=True)
    )'''
   
    '''r=Restaurant.objects.annotate(nsales=Count('sales'))
    r=r.annotate(
        is_popular=Case(
            When(nsales__gt=8,then=True),default=False
            )
        )
    print(r.values('nsales','is_popular'))
    print(r.filter(is_popular=True))'''
    #pprint(connection.queries)
    #rest average rating >3.5
    #rest has more than 1 rating
    
    
    #annoate rest with avg ratings and num of ratings
    '''r = Restaurant.objects.annotate(
        avg=Avg('ratings__rating'),
        num_ratings=Count('ratings__pk')
    )
    r=r.annotate(
        highly_rated=Case(
            When(avg__gt=3.5,num_ratings__gt=1,then=True),default=False
        )
    )
    r=r.annotate(
        rating_bucket=Case(
            When(avg__gt=3.5,then=Value('highly Rated')),
            When(avg__range=(2.5,3.5),then=Value('avg Rated')),
            When(avg__lt=2.5,then=Value('bad Rated')),
        ) each 10 day peroid , starting from the frist sale up till last
    )
    #print(r.values('avg','num_ratings'))
    print(r.filter(rating_bucket='highly Rated'))
    print(r.filter(rating_bucket='avg Rated'))
    print(r.filter(rating_bucket='bad Rated'))'''
    
    #assign continets to each rest
    '''types=Restaurant.TypeChoices
    rest=Restaurant.objects.annotate(
        continent=Case(
            When(Q(restaurant_type=types.ITALIAN) | Q(restaurant_type=types.GREEK), then=Value("europe")),
            When(Q(restaurant_type=types.INDIAN) | Q(restaurant_type=types.CHINESE), then=Value("asia")),
            When(restaurant_type=types.MEXICAN, then=Value("NorthAmerica")),
            default=Value('N/A')
         ))
    
    eu=Q(restaurant_type=types.ITALIAN) | Q(restaurant_type=types.GREEK)
    asia=Q(restaurant_type=types.INDIAN) | Q(restaurant_type=types.CHINESE)
    northame=Q(restaurant_type=types.MEXICAN)
    rest=Restaurant.objects.annotate(
        continent=Case(
            When(eu, then=Value("europe")),
            When(asia,then=Value("asia")),
            When(northame,then=Value("NorthAmerica")),
            default=Value('N/A')))
                 
                 
    print(rest.filter(continent="asia"))'''
    
    #aggreating total sales over each 10 day peroid starting from frist day to last
    #1-10
    #11-20
    first_sale=Sale.objects.aggregate(first_sale_date=Min('datetime'))['first_sale_date']
    last_sale=Sale.objects.aggregate(last_sale_date=Max('datetime'))['last_sale_date']
    
    #generate a list of dates each 10 days apart
    dates=[]
    count=itertools.count()
    while(dt := first_sale + timezone.timedelta(days=10*next(count)))<=last_sale:
        dates.append(dt)
    whens=[
        When(datetime__range=(dt, dt+timezone.timedelta(days=10)),then=Value(dt.date()))
        for dt in dates
    ]
    case=Case(
        *whens,
        output_field=CharField()
    )
    s=Sale.objects.annotate(
        daterange=case
    ).values('daterange').annotate(total_sales=Sum('income'))
    pprint(s)
    
    
    
    