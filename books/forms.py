from django import forms
from django.forms import TextInput, Select, ClearableFileInput
from . import models


class CreateBookForm(forms.Form):
    choiceList = models.Book.GENRE
    isbn = forms.CharField(label = 'ISBN:', max_length = 20, widget=TextInput(attrs={'autofocus':True, 'class':'form-control', 'required':True,'placeholder':'ISBN...' }))
    
    book_name = forms.CharField(label = 'Book Name:', max_length = 50, widget=TextInput(attrs={'class':'form-control', 'required':True,'placeholder':'Name...' }))
    
    author = forms.CharField(label = 'Author:', max_length = 50, widget=TextInput(attrs={'class':'form-control', 'required':True,'placeholder':'Author...' }))
    
    genre = forms.ChoiceField(label = 'Genre:',choices = choiceList,widget=Select(attrs={'class':'form-control','required':True}))
    
    book_cover = forms.ImageField(label = 'Book Cover:', widget=ClearableFileInput(attrs={'required':False,'style':'color:white;'}))

    
class EditBookForm(forms.Form):
    choiceList = models.Book.GENRE
    isbn = forms.CharField(label = 'ISBN:', max_length = 20, widget=TextInput(attrs={'autofocus':True, 'class':'form-control', 'required':False }))
    
    book_name = forms.CharField(label = 'Book Name:', max_length = 50, widget=TextInput(attrs={'class':'form-control', 'required':False }))
    
    author = forms.CharField(label = 'Author:', max_length = 50, widget=TextInput(attrs={'class':'form-control', 'required':False }))
    
    genre = forms.ChoiceField(label = 'Genre:',choices = choiceList,widget=Select(attrs={'class':'form-control','required':False}))
    
    book_cover = forms.ImageField(label = 'Book Cover:', widget=ClearableFileInput(attrs={'required':False,'style':'color:white;'}))