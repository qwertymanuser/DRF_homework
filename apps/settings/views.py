from django.shortcuts import render
from .models import Setting,BlogDetail,Blog,BooksDetail,Books,Image

# Create your views here.

def index(request):
    setting = Setting.objects.latest("id")
    context = {
        "setting":setting
    }
    return render(request, "index.html", context)

def blog_detail(request):
    blog_detail = BlogDetail.objects.latest("id")
    context = {
        "setting":blog_detail,
    }
    return render(request, "blog-detail.html", context)


def blog(request):
    blog = Blog.objects.latest("id")
    context = {
        "blog": blog,

    }
    return render(request, "blog.html", context)

def books_detail(request):
    books_detail = BooksDetail.objects.latest("id")
    context = {
        "books_detail": books_detail,

    }
    return render(request, "books-detail.html", context)


def books(request):
    books = Books.objects.latest("id")
    context = {
        "books": books,
    }
    return render(request, "books.html", context)


def image(request):
    image = Image.objects.latest("id")
    context = {
        "image": image,

    }
    return render(request, "image.html", context)

