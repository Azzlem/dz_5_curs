from django import forms

from catalog.models import Article, Product, Version


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user_creator',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        if cleaned_data in ['казино', 'криптовалюта',
                            'крипта', 'биржа', 'дешево',
                            'бесплатно', 'обман', 'полиция', 'радар']:
            raise forms.ValidationError("Недопустимое название продукта")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
