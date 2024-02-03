from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name in self.fields:
      self.fields[field_name].widget.attrs.update({'class': 'form-control'})
    self.fields['description'].widget.attrs.update({'rows': '3'})  # Adjust rows attribute for textarea

  class Meta:
    model = Product
    fields = ['name', 'quantity', 'price', 'description', 'image']
    labels = {
      'name': 'Product Name',
      'quantity': 'Quantity Available',
      'price': 'Price',
      'description': 'Description',
      'image': 'Product Image',
    }