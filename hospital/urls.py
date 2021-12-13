from django.urls import path
from .views import doctor


urlpatterns = [ 
    # path('', views.index, name='index'),
    path('doctors/', doctor.DoctorsView.as_view(), name='index'),
    # path('<int:id>/', views.show, name='show'),
    path('doctors/<int:id>/', doctor.DoctorView.as_view(), name='show')
]