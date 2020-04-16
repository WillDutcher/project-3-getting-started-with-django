from django import forms

from .models import Day, Meal
################################### from .forms import MealForm

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['day']
        labels = {'day': ''}

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal']
        labels = {'meal': ' '}
        widgets = {'meal': forms.Textarea(attrs={'cols': 80})}
