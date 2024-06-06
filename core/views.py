from django.shortcuts import render
from django.http import HttpResponse
from core.forms import RatingForm,RestaurantForm


def index (request):
    if request.method=='POST':
        form=RestaurantForm(request.POST or None)
        if form.is_valid():
            #form.save()
            print(form.cleaned_data)
        else:
            return render(request,'index.html',{'form':form})
    context={'form':RestaurantForm()}
    return render(request,'index.html',context)
