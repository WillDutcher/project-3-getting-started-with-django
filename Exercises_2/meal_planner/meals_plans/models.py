from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Day(models.Model):
    """Day that meal is being prepped."""
    day = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.day

class Meal(models.Model):
    """Meals being prepared."""
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    meal = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'meals'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.meal) > 50:
            return f"{self.meal[:50]}..."
        else:
            return f"{self.meal}"
