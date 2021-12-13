# library/urls.py
from django.urls import path
from .views import book
from .views import author


urlpatterns = [ 
    # path('', views.index, name='index'),
    path('books/', book.BooksView.as_view(), name='index'),
    # path('<int:id>/', views.show, name='show')
    path('books/<int:id>/', book.BookView.as_view(), name='show'),
    path('authors/', author.AuthorsView.as_view(), name='index'),
    path('authors/<int:id>/', author.AuthorView.as_view(), name='Author-detail')
]
