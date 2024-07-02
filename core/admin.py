from django.contrib import admin

from .models import *

admin.site.register(Rating)
admin.site.register(Restaurant)
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Order)