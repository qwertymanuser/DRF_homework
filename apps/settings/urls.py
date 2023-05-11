from django.urls import path
from .views import index, blog_detail,blog,books_detail,books,image


urlpatterns = [
    path('', index, name = "index"),
    path('blog_detail/', blog_detail, name = "blog_detail"),
    path('blog/', blog, name = "blog"),    
    path('books_detail/', books_detail, name = "books-detail"),
    path('books/', books, name = "books"),         
    path('image/', image, name = "image"),        
]