from django import forms
from .models import Book,Author, Publisher

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_date','publisher']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date']
        
class BookFormWithoutAuthor(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['author']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'city', 'state_province', 'country', 'website']
class BookFormWithoutAuthorPublisher(forms.ModelForm):  
        class Meta:
            model=Book 
            exclude=['author','publisher']