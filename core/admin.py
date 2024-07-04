from django.contrib import admin

from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display=['id','name']
    
class RatingAdmin(admin.ModelAdmin):
    list_display=['id','rating']
    
class CommentAdmin(admin.ModelAdmin):
    list_display=['text','object_id',"content_type",'content_object']

admin.site.register(Rating,RatingAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment,CommentAdmin)