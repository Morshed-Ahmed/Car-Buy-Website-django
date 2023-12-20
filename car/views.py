from django.shortcuts import render,redirect, get_object_or_404
from car.models import Car,CarBuy,Comment
from brand.models import Brand
from django.contrib import messages
from . import forms



# Create your views here.
def index(request,brand_name = None):
    data = Car.objects.all()
    brands = Brand.objects.all()
    if brand_name == 'all':
        data = Car.objects.all()
    elif brand_name is not None:
        bt = Brand.objects.get(name = brand_name)
        print(data)
        data = Car.objects.filter(brand = bt)
        print(data)
    return render(request,'home.html',{'data':data,'brands':brands})


def car_details(request,car_id):
    data = Car.objects.filter(id = car_id)
    crr = Car.objects.get(id = car_id)
    comment_data = Comment.objects.filter(post=car_id)
    
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment =form.save(commit=False)
            new_comment.post = crr
            new_comment.save()
                                
            return render(request,'car_details.html',{'data':data,'form':form,'comment_data':comment_data})
    else:
        form = forms.CommentForm()
    return render(request,'car_details.html',{'data':data,'form':form,'comment_data':comment_data})




def buy_now(request,car_id):
    buy = 1
    car_quantity = Car.objects.get(id = car_id)
    print(car_quantity.quantity)
    if car_quantity.quantity >= buy:
        car_quantity.quantity -= buy
        car_quantity.save()
        use = request.user

        buying = CarBuy()
        buying.name = request.user
        buying.buy_cars = Car.objects.get(id = car_id)
        buying.save()
        
        messages.success(request, 'Buy this car Successfully')
        
        return redirect('car_details',car_id)
    else:
        messages.error(request, 'Car quantity not available')     
        return redirect('car_details',car_id)