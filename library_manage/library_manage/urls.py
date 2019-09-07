from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from library import views
urlpatterns = [
    path('', views.index),
    # url('^index/', views.index),
    path('index/', views.index),
    path('test/', views.test),

    path('publisher_list/', views.publisher_list),
    path('add_publisher/', views.add_publisher),
    path('delete_publisher/', views.delete_publisher),
    path('edit_publisher/', views.edit_publisher),

    path('book_list/', views.book_list),
    path('add_book/', views.add_book),
    path('delete_book/', views.delete_book),
    path('edit_book/', views.edit_book),

    path('author_list/', views.author_list),
    path('add_author/', views.add_author),
    path('edit_author/', views.edit_author),
    path('delete_author/', views.delete_author),
]
