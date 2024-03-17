from django import forms

import re

from catalog.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
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


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
