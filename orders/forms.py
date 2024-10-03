from django import forms
from .models import PizzaOrder

class PizzaOrderForm(forms.ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['pizza_type', 'special_instructions']
        widgets = {
            'pizza_type': forms.Select(choices=PizzaOrder.PIZZA_CHOICES),
            'special_instructions': forms.Textarea(attrs={'rows': 3}),
        }

