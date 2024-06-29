from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db.models.functions import Upper,Length,Concat,Coalesce
from django.db.models import Count,Avg,Min,Max,Sum,Case,When
from django.db.models import F,Q
from django.db import connection
from pprint import pprint 
import random
def run():
    it=Restaurant.TypeChoices.ITALIAN
    
    rs=Restaurant.objects.annotate(
        is_it=Case(
            When(restaurant_type=it,then=True),default=False)
        )
    print(
        rs.filter(is_it=True)
    )