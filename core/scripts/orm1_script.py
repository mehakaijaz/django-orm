from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.contrib.auth.models import User


def run():
    # restaurant=Restaurant.objects.first()
    # print(restaurant.sales.all())
    # pprint(connection.queries)
    
    # Sale.objects.create(
    #   restaurant=Restaurant.objects.first(),income=2.44,
    #   datetime=timezone.now()  
    # )
    # Sale.objects.create(
    #   restaurant=Restaurant.objects.first(),income=34,
    #   datetime=timezone.now()  
    # )
    # Sale.objects.create(
    #   restaurant=Restaurant.objects.first(),income=78,
    #   datetime=timezone.now()  
    # )
   
   #fetch or create data
   #get_or_create()method
    # user=User.objects.last()
    # restaurant=Restaurant.objects.last()
    # rating, created=Rating.objects.get_or_create(
    #     restaurant=restaurant,
    #     user=user,
    #     rating=4
    # )
    
    # if created:
        #send email
        
    #pprint(connection.queries)
    
    user=User.objects.last()
    restaurant=Restaurant.objects.last()
    
    rating=Rating(
        restaurant=restaurant,
        user=user,
        rating=6
    )
    rating.full_clean()
    rating.save()