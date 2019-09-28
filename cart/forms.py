from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from core.get_config import get_config


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 100)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartSubmitOrder(forms.Form):
    """Форма сабмита заказа"""
    _contact = get_config()['contactTypeList']

    contacts = [(key, value) for key, value in _contact.items()]

    contact_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'uk-input', 'id': 'contact_name'}),
        min_length=3,
        max_length=255,
        label='Введите ваше имя'
    )
    contact_type = forms.ChoiceField(
        widget=forms.widgets.Select(attrs={'id': 'contact_type', 'class': 'uk-select'}),
        choices=tuple(contacts),
        label='Выберите удобный способ связи'
    )
    contact_data = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'uk-input', 'id': 'contact_data'}),
        min_length=4,
        max_length=512,
        label='Введите контактные данные'
    )
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(attrs={'id': 'captcha'}),
        label=''
    )
