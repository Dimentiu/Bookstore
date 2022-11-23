from django.urls import path

from . import views
from .views import author_info, authors_list, book_info, books_list, index, publisher_info, publishers_list, \
    stores_info, stores_list

app_name = 'bookstore'
urlpatterns = [
    path('', index, name="index"),
    path('books/', books_list, name='books'),
    path('books/<int:id>/', book_info, name='books_info'),
    path('authors/', authors_list, name="authors"),
    path('authors/<int:id>/', author_info, name='author_info'),
    path('stores/', stores_list, name="stores"),
    path('stores/<int:id>', stores_info, name="stores_info"),
    path('publishers/', publishers_list, name='publishers'),
    path('publishers/<int:pk>', publisher_info, name='publisher_info'),
    path('authors/create_author', views.AuthorCreateView.as_view(), name='create_author'),
    path('authors/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='update_author'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='delete_author'),
    path('authors/pagination/', views.AuthorListView.as_view(), name='pagination_author'),
    path('authors/pagination/<int:pk>/detail/', views.AuthorDetailView.as_view(), name='detail_author')
]
