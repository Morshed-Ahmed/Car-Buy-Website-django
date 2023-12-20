from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('brand/<str:brand_name>/',views.index, name = 'brand_wise_product'),
    path('car/<int:car_id>/',views.car_details, name = 'car_details'),
    path('car/buy_now/<int:car_id>/', views.buy_now, name='buy_now'),
]
