import random 
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Restaurant,Rating,Sale

class Command(BaseCommand):
    help='creates application data'
    
    def handle(self, *args, **kwargs):
        #get or create an admin user
        user=User.objects.filter(username='admin')
        if not user.exists():
            user=User.objects.create_superuser(username='admin',password='text')
        else:
            user=user.first()
        restaurants=[
            {'name':'Pizzaire1','date_opened':timezone.now() - timezone.timedelta(days=20),'restaurant_type':Restaurant.TypeChoices.INDIAN,'latitude': 41.902782, 'longitude':  12.496366},
            {'name':'Pizzaire2','date_opened':timezone.now() - timezone.timedelta(days=26),'restaurant_type':Restaurant.TypeChoices.ITALIAN,'latitude': 41.902782, 'longitude':  12.496366},
            {'name':'Pizzaire3','date_opened':timezone.now() - timezone.timedelta(days=28),'restaurant_type':Restaurant.TypeChoices.CHINESE,'latitude': 41.902782, 'longitude':  12.496366},
            {'name':'Pizzaire4','date_opened':timezone.now() - timezone.timedelta(days=2),'restaurant_type':Restaurant.TypeChoices.MEXICAN,'latitude': 41.902782, 'longitude':  12.496366},
            {'name':'Pizzaire5','date_opened':timezone.now() - timezone.timedelta(days=54),'restaurant_type':Restaurant.TypeChoices.FASTFOOD,'latitude': 41.902782, 'longitude':  12.496366},
            {'name':'Pizzaire6','date_opened':timezone.now() - timezone.timedelta(days=32),'restaurant_type':Restaurant.TypeChoices.INDIAN,'latitude': 41.902782, 'longitude':  12.496366}  
        ]
        
        Restaurant.objects.all().delete()
        for r in restaurants:
            Restaurant.objects.create(**r)
            
        restaurants=Restaurant.objects.all()
        
        #create some rating
        for _ in range(30):
            Rating.objects.create(
                restaurant=random.choice(restaurants),
                user=user,
                rating=random.randint(1,5)
            )
        
        #create sales
        for _ in range(300):
            Sale.objects.create(
                restaurant=random.choice(restaurants),
                income=random.randint(1,300),
                datetime=timezone.now()-timezone.timedelta(days=random.randint(1,50))
            )
        
        return super().handle(*args, **kwargs)