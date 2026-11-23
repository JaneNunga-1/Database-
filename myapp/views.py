from django.shortcuts import render, redirect

from myapp.models import Book
from myapp.my_form import BookForm


# Create your views here.
def view_book(request):
    books = Book.objects.all()
    return render(request, 'view_book.html', {'books': books})

def add_book(request):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('view_book')  # <-- Remove {'form': form} here!
        else:
            form = BookForm()

        return render(request, 'add_book.html', {'form': form})

        # Book.objects.create(
        #    title="River and the source",
        #    isbn="yui090898",
        #    cost=900,
        #    year=1990
        # )
        # Book.objects.create(
        #     title="River and the source",
        #     isbn="yui090898",
        #     cost=900,
        #     # year=1990
        # )


