from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('',views.charge, name='charge'),
    path('verify/<str:reference>', views.verify, name='verify'),

]