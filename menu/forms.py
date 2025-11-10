from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(label="Телефон", max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Адрес", widget=forms.Textarea(attrs={"class": "form-control", "rows": 2}))
    comment = forms.CharField(label="Комментарий", required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 2}))
