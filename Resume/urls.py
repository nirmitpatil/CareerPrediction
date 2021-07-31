from django.urls import path
from . import views

urlpatterns =[
        path('resume',views.resume,name='resume'),
        path('resume1',views.resume1,name='resume1'),
        path('resume2',views.resume2,name='resume2'),
        path('resume3',views.resume3,name='resume3'),
        path('resume4',views.resume4,name='resume4'),
        path('resume5',views.resume5,name='resume5'),
]