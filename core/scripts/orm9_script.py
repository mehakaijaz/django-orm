#transactions

from django.contrib.auth.models import User
from core.models import Restaurant,Rating,Sale,Staff,StaffRestaurant
from django.utils import timezone
from django.db.models.functions import Upper,Length,Concat,Coalesce
from django.db.models import OuterRef,Subquery,Exists
from django.db.models import F,Q,Value,CharField
from django.db import connection
from pprint import pprint 
import random
import itertools

