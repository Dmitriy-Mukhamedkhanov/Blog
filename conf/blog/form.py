from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class FormCreateObject(forms.Form):
    name = forms.CharField(label='Название картинки')
    image = forms.ImageField(label="Изoбpaжeниe")
    description = forms.CharField(label='Описание картинки')

class FormChangeObject(forms.Form):
    name = forms.CharField(label='Новое название картинки', required=False)
    image = forms.ImageField(label="Новое изoбpaжeниe", required=False)
    description = forms.CharField(label='Новое описание картинки', required=False)