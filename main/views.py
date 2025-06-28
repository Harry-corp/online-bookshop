from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Category, Author
from django.views import generic
from .forms import BookFilterForm

def main(request):
    newest_books = Book.objects.all().order_by("published_date")[:4]
    top_categories = Category.objects.all()[:3]
    popular_authors = Author.objects.all()[:4]
    context = {
        "new_books":newest_books,
        "top_categories":top_categories,
        "authors":popular_authors
    }
    return render(request,'index.html',context)

def store(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = BookFilterForm(request.POST)
        if form.is_valid():
            min_price = form.cleaned_data["min_price"]
            max_price = form.cleaned_data["max_price"]
            category = form.cleaned_data["category"]    
            print(form.cleaned_data)

            if category:
                books = Book.objects.filter(price__gte=min_price,price__lte=max_price, category=category)
                return render(request,"store.html",{"form":form,"books":books,"categories":categories})
            
            books = Book.objects.filter(price__gte=min_price,price__lte=max_price)
            return render(request,"store.html",{"form":form,"books":books,"categories":categories})
        
    form = BookFilterForm()
    books = Book.objects.all()
    return render(request,"store.html",{"form":form,"books":books,"categories":categories})

def authors(request):
    authors = Author.objects.all()
    return render(request,"authors.html",{"authors":authors})

def contact(request):
    return render(request,"contact.html")

class Author_DetailView(generic.DetailView):
    template_name = "details/author-detail.html"
    model = Author
    context_object_name = "author"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_books = Book.objects.filter(author=self.object)
        context['author_books'] = author_books
        popular_authors = Author.objects.all().exclude(pk=self.object.pk)[:4]
        context["popular_authors"] = popular_authors
        return context

class Book_DetailView(generic.DetailView):
    template_name = "details/book-detail.html"
    model = Book
    context_object_name = "book"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_books = Book.objects.filter(category=self.object.category).exclude(pk=self.object.pk)[:3]
        if len(related_books) == 0:
            related_books = Book.objects.all().exclude(pk=self.object.pk)[:3]
        context["related_books"] = related_books
        return context
def categories(request):
    return render(request,"index.html")