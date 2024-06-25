from django.shortcuts import render
from django.http import HttpResponse
from core.forms import RatingForm,RestaurantForm
from core.models import Restaurant,Rating,Sale,StaffRestaurant
from django.db.models import Sum,Prefetch
from django.utils import timezone

# def index (request):
#    """if request.method=='POST':
#         form=RestaurantForm(request.POST or None)
#         if form.is_valid():
#             #form.save()
#             print(form.cleaned_data)
#         else:
#             return render(request,'index.html',{'form':form})
#     context={'form':RestaurantForm()}
#    # rest=Restaurant.objects.all()#prefetch_related('ratings','sales')
#     rest=Restaurant.objects.filter(name__startswith='c').prefetch_related('ratings','sales')
#     context={'rest':rest}
#    # ratings=Rating.objects.select_related('restaurant')
#     # ratings=Rating.objects.only('rating','restaurant__name').select_related('restaurant')
#     # context={'ratings':ratings}
#     #get all 5-star ratings,and fetch all the sales with it
#     month_ago=timezone.now()-timezone.timedelta(days=20)
#     monthly_sales=Prefetch('sales',
#                            queryset=Sale.objects.filter(datetime__gte=month_ago))
#     rest=Restaurant.objects.prefetch_related('ratings',monthly_sales).filter(ratings__rating=5)
#     rest=rest.annotate(total=Sum('sales__income'))
#          # .annotate(total=Sum('sales__income')))
#     print([r.total for r in rest])
#     return render(request,'index.html')"""

def index(request):
    jobs=StaffRestaurant.objects.prefetch_related("restaurant",'staff')
    
    for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name)
    
    return render(request,'index.html')