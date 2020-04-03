from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 4)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label=False, choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget = forms.Select(attrs = {'onchange' : "form.submit();"}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
