from django import forms
from .models import Product
# from .models import Category

class AddNewProduct(forms.ModelForm):
    # category =forms.ModelChoiceField(Category.objects.all())

    class Meta:
        model=Product
        fields='__all__'