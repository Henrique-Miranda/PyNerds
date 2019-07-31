from django import forms

class NLetterForm(forms.Form):
    your_email = forms.EmailField(label='Seu melhor E-mail', max_length=100)
