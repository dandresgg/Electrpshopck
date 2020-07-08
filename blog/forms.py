from django import forms

class SearchForm(forms.Form):
    digita_tu_busqueda = forms.CharField()