from django.urls import path
from .views import food


urlpatterns = [ 
    # path('', views.index, name='index'),
    path('foods/', food.FoodsView.as_view(), name='index'),
    # path('<int:id>/', views.show, name='show'),
    path('foods/<int:id>/', food.FoodView.as_view(), name='show')
]