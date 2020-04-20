"""
Used to define the data we want to manage in our app.
"""

from django.db import models
from django.contrib.auth.models import User

class Pizza(models.Model):
    """A pizza someone is creating."""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """Something specific learned about a topic."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.name) > 50:
            return f"{self.name[:50]}..."
        else:
            return f"{self.name}"
