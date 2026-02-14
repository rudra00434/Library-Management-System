from django.urls import path
from .import views  
from .views import BookDetailView,  BookListView
urlpatterns = [
    path('', views.book_list, name='book_list_fbv'),
    path('fbv/books/<int:book_id>/', views.book_detail, name='book_detail_fbv'),

    path('cbv/books/', BookListView.as_view(), name='book_list_cbv'),
    path('cbv/books/<int:pk>/', BookDetailView.as_view(), name='book_detail_cbv'),

    path('authors/', views.author_list, name='author_list'),
    path('author/<int:author_id>/books/', views.book_by_author, name='book_by_author'),
    path('add_book/',views.add_book,name='add_book'),
    path('add_book_and_author/',views.add_book_and_author,name='add_book_and_author'),
    path('add_book_author_publisher/',views.add_book_author_publisher,name='add_book_author_publisher'),
]
