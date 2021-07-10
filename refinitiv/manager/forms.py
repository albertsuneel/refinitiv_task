from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput())


class AddUserForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput())


class RequestResponseForm(forms.Form):
    id = forms.CharField(max_length=25)
    comments = forms.CharField(max_length=500)
    status = forms.IntegerField()

