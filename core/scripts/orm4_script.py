from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db import connection
from pprint import pprint 
import random

def run():
    staff, created=Staff.objects.get_or_create(name='joe doe')
    staff.restaurants.set(Restaurant.objects.all()[:10],
                         through_defaults={'salary':random.randint(20_000,80_000)})
    # print(staff)
    # staff.restaurants.clear()
    # restaurant=Restaurant.objects.first()
    # staff.restaurants.add(restaurant,through_defaults={'salary':28000})
    # StaffRestaurant.objects.create(
    #     staff=staff,restaurant=restaurant,salary=2_89_000
    # )
    
    # StaffRestaurant.objects.create(
    #     staff=staff,restaurant=restaurant2,salary=6_09_000
    # )
    # staff_resturant=StaffRestaurant.objects.filter(staff=staff)
    # for s in staff_resturant:
    #     print(s.salary)
    #print(type(staff.restaurant))
    """print(staff.restaurant.add(Restaurant.objects.first()))
    print(staff.restaurant.all())
    print(staff.restaurant.count())
    staff.restaurant.remove(Restaurant.objects.first())
    staff.restaurant.clear()
    staff.restaurant.set(Restaurant.objects.all()[:9])
    print(staff.restaurant.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN))"""
    
    # restaurant=Restaurant.objects.get(pk=19)
    # print(restaurant.staff_set.all())