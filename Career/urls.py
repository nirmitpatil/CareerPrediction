from django.urls import path
from . import views

urlpatterns =[
        path('',views.home,name='home'),
        path('about',views.about,name='about'),
        path('iq',views.iq,name='iq'),
        path('iq_func',views.iq_func,name='iq_func'),
        path('general_func',views.general_func,name='general_func'),
        path('advance_func',views.advance_func,name='advance_func'),
        path('review_display/<str:C_id>/',views.review_display,name='review_display'),
]