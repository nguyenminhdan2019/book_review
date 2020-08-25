from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    BooksListView,
    SearchBookListView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('books', BooksListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('search-book-results/', SearchBookListView.as_view(), name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

