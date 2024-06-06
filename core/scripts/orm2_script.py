#update and delete query
from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
 
def run():
    # restaurant=Restaurant.objects.first()
    # print(restaurant.name)
    
    # restaurant.name='abc'
    # restaurant.save(update_fields=['name'])
    #single object updation
    # restaurant= Restaurant()
    # restaurant.name='My Italian Restaurant'
    # restaurant.latitude=50.2
    # restaurant.longitude=50.2
    # restaurant.date_opened=timezone.now()
    # restaurant.restaurant_type=Restaurant.TypeChoices.ITALIAN
    # restaurant.save()
    # print(connection.queries)
    
    #all objects updation
    # restaurants=Restaurant.objects.all()
    # restaurants.update(
    #     date_opened=timezone.now(),
    #     latitude=90
    # )
    #filtering qs with startswith lookup field
    # restaurants=Restaurant.objects.filter(name__startswith='p')
    # print(restaurants.update(
    #     date_opened=timezone.now()-timezone.timedelta(days=365),
    #     website='https://www.test.cpm'
    # ))
    
    #deleting qs
    # restaurant=Restaurant.objects.first()
    # print(restaurant.pk)
    
    # print(restaurant.ratings.all())
    # print(restaurant.delete())
    
    
    
    
    print(connection.queries)