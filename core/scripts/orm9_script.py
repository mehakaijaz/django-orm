#transactions

from django.contrib.auth.models import User
from core.models import *
from django.utils import timezone
from django.db.models.functions import Upper,Length,Concat,Coalesce
from django.db.models import OuterRef,Subquery,Exists
from django.db.models import F,Q,Value,CharField
from django.db import connection,transaction
from pprint import pprint 
import random
import itertools
import time
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
def run():
    # with transaction.atomic():
    #     book=Product.objects.select_for_update().get(name='book')
    #     time.sleep(70)
    """rest=Restaurant.objects.first()
    comment=Comment.objects.create(text="awful",content_object=rest)
    print(comment)
    print(comment.__dict__)
    # for comment in comments:
    #     print(comment.content_object)
    ctype=comment.content_type
    print(ctype)
    
    model=ctype.get_object_for_this_type(pk=comment.object_id)
    print(model)"""
    
    """rest=Restaurant.objects.get(pk=4)
    comments=rest.comments.all()
    print(comments)"""
    
    rest=Restaurant.objects.first()
    user=User.objects.first()
    rating=Rating.objects.create(
        restaurant=rest,
        user=user,
        rating=5
    )
    print(rating)