from django.urls import path
from .views import main,store,contact,authors,Author_DetailView,Book_DetailView,categories

urlpatterns = [
    path('',main,name='main'),
    path('store/', store, name='store'),
    path('authors/',authors,name="authors"),
    path('categories/',categories,name="categories"),
    path('contact/', contact, name='contact'),
    path('book/<slug>/', Book_DetailView.as_view(), name='book_detail'),
    path('author/<slug>/',Author_DetailView.as_view(),name="author_detail")
]    