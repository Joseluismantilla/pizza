from django.db import models

class PizzaOrder(models.Model):
    PIZZA_CHOICES = [
        ('Margherita', 'Margherita'),
        ('Pepperoni', 'Pepperoni'),
        ('Vegetarian', 'Vegetarian'),
    ]
    pizza_type = models.CharField(max_length=20, choices=PIZZA_CHOICES)
    special_instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pizza_type} - {self.special_instructions[:20]}"

