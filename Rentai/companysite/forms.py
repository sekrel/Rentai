from django import forms
from .models import Creation

class ProductForm(forms.ModelForm):
    class Meta:
        model = Creation
        fields = '__all__'



# class AddCreationForm(forms.Form):
#     text = forms.CharField(max_length=255)
#     tag = forms.CharField(max_length=255)
#     img = forms.ImageField