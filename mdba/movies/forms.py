from django import forms

class SearchForm(forms.Form):
    """Django form for movie search"""
    
    title = forms.CharField(label='Movie Title', max_length=100, required=False)
    year = forms.IntegerField(label='Release Year', required=False)
    actor = forms.CharField(label='Actor', max_length=100, required=False)
    director = forms.CharField(label='Director', max_length=100, required=False)
    genre = forms.CharField(label='Genre', max_length=100, required=False)
    lang = forms.CharField(label='Language', max_length=100, required=False)
    country = forms.CharField(label='Country', max_length=100, required=False)
    plot = forms.CharField(label='Plot Keywords', max_length=100, required=False)
