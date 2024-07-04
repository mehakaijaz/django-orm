from django.shortcuts import render ,redirect
from django.http import HttpResponse
from core.forms import RatingForm,RestaurantForm,ProductOrderForm
from core.models import *
from django.db.models import Sum,Prefetch
from django.utils import timezone
from django.db import transaction
from functools import partial
"""def index (request):
   if request.method=='POST':
        form=RestaurantForm(request.POST or None)
        if form.is_valid():
            #form.save()
            print(form.cleaned_data)
        else:
            return render(request,'index.html',{'form':form})
    context={'form':RestaurantForm()}
   # rest=Restaurant.objects.all()#prefetch_related('ratings','sales')
    rest=Restaurant.objects.filter(name__startswith='c').prefetch_related('ratings','sales')
    context={'rest':rest}
   # ratings=Rating.objects.select_related('restaurant')
    # ratings=Rating.objects.only('rating','restaurant__name').select_related('restaurant')
    # context={'ratings':ratings}
    #get all 5-star ratings,and fetch all the sales with it
    month_ago=timezone.now()-timezone.timedelta(days=20)
    monthly_sales=Prefetch('sales',
                           queryset=Sale.objects.filter(datetime__gte=month_ago))
    rest=Restaurant.objects.prefetch_related('ratings',monthly_sales).filter(ratings__rating=5)
    rest=rest.annotate(total=Sum('sales__income'))
         # .annotate(total=Sum('sales__income')))
    print([r.total for r in rest])
    return render(request,'index.html')"""

def email_user(email):
    print(f" dear {email}, thank uh for your order.")


def index(request):
    jobs=StaffRestaurant.objects.prefetch_related("restaurant",'staff')
    
    for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name)
    
    return render(request,'index.html')

def orderproduct(request):
    if request.method=='POST':
        form=ProductOrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                product=Product.objects.select_for_update().get(
                    id=form.cleaned_data['product'].pk
                    )
                import time 
                time.sleep(25)
                order=form.save()
                #server clash
                # import sys
                # sys.exit(1)
                order.product.num_in_stock -= order.num_of_items
                order.product.save()
            transaction.on_commit(partial(email_user, 'mehakaijaz@gmail.com'))
            return redirect('orderproduct')
    
        else:
            context={'form':form}
            return render(request,'order.html',context)
    form=ProductOrderForm()
    context={'form':form}
    return render(request,'order.html',context)