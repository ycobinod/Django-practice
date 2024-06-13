from . import views, api_views
from django.urls import path 
urlpatterns = [path('books/', views.book_list, name='book_list'),
               path('book/<int:pk>/', views.book_detail,name='book_detail'),
               #path('api/all_books/',api_views.AllBooks.as_view(),name='all_books')
              path('api/login',api_views.Login.as_view(),name='login')
               ]