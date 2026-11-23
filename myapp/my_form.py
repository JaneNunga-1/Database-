from django import forms

from myapp.models import Book


# inherits from forms inside it we have a class called Model Form
class BookForm(forms.ModelForm):
    class Meta:
        # u are inheriting a book
        model = Book
        # what fields u want displayed
        fields = ('title', 'isbn', 'cost', 'category', 'published', 'year')
