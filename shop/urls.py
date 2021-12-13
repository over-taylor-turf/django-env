from django.urls import path
from .views import gift


urlpatterns = [ 
    # path('', views.index, name='index'),
    path('gifts/', gift.GiftsView.as_view(), name='index'),
    # path('<int:id>/', views.show, name='show'),
    path('gifts/<int:id>/', gift.GiftView.as_view(), name='show')
]