from django import forms

import re

from catalog.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_current':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')

        if bool(re.search('|'.join(FORBIDDEN_WORDS), cleaned_data.lower())):
            raise forms.ValidationError('Были использованы запрещенные слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        if bool(re.search('|'.join(FORBIDDEN_WORDS), cleaned_data.lower())):
            raise forms.ValidationError('Были использованы запрещенные слова')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
