from core.models import Restaurant,Rating
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    #instantiate
    # restaurant=Restaurant()
    # restaurant.name='My Italian Restaurant'
    # restaurant.latitude=50.2
    # restaurant.longitude=50.2
    # restaurant.date_opened=timezone.now()
    # restaurant.restaurant_type=Restaurant.TypeChoices.ITALIAN
    
    # restaurant.save()
    
    #querying data=getting all rows from a table
    # restaurants=Restaurant.objects.all()# this gives queryset
    # restaurant=Restaurant.objects.first()# this gives name of first row
    # print(restaurants)
    # print(restaurant)
    # print(connection.queries)
    
    #indexing into django-queryset
    # restaurants=Restaurant.objects.all()[0]
    # print(restaurants)
    # print(connection.queries)
    
    #creating records using model.objects.create()
    # Restaurant.objects.create(
    #     name='pixa shop',
    #     date_opened=timezone.now(),
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN,
    #     latitude=67.7,
    #     longitude=90.9
    # )
    # print(connection.queries)#query execution
    
    # restaurants=Restaurant.objects.count()#gives no of rows in db table
    # print(restaurants)
    # print(connection.queries)
    
    # restaurants=Restaurant.objects.last()#gives name of last row
    # print(restaurants)
    # print(connection.queries)

    #filtering records-> filter()
    #print(Rating.objects.filter(rating=3))

    #print(Rating.objects.filter(rating__gte=3))#greater than or equal to 3
     #filtering records-> exclude()
    #print(Rating.objects.exclude(rating__lte=3))#less than or equal to 3

    #updating existing records with model save() method
    # restaurant=Restaurant.objects.first()
    # restaurant.name='drtfyguhijop'
    # restaurant.save()
    # print(restaurant.name)
    # pprint(connection.queries)

    #query related records
    # rating=Rating.objects.first()
    # print(rating.restaurant)
    

