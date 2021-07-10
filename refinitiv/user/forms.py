from django import forms


class RequestForm(forms.Form):
    name = forms.CharField(max_length=25)
    position = forms.CharField(max_length=5)
    currency = forms.CharField(max_length=5)
    amount = forms.IntegerField()
    branch = forms.CharField(max_length=5)


class RequestEditForm(forms.Form):
    id = forms.CharField(max_length=25)
    name = forms.CharField(max_length=25)
    position = forms.CharField(max_length=5)
    currency = forms.CharField(max_length=5)
    amount = forms.IntegerField()
    branch = forms.CharField(max_length=5)
