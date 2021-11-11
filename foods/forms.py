from django.forms import ModelForm, models
from .models import Food

class AddFoodForm(ModelForm):
    class Meta:
        model = Food
        fields= ['food_name', 'food_image']