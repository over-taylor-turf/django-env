from django.urls import path
from .views import dorm


urlpatterns = [ 
    path('dorms/', dorm.DormsView.as_view(), name='index'),
    path('dorms/<int:id>/', dorm.DormView.as_view(), name='show')
]