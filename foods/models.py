from django.db import models


CATEGORY= (
    ('VEGITARIAN', 'Vegitarian'),
    ('CHINESE', 'Chinese'),
    ('MEAL', 'Meal'),
    ('ICECREAMS', 'Icecreams'),
    ('SHAKES', 'Shakes'),
    ('SOUPS', 'Soups'),
)

class Food(models.Model):
    food_name = models.CharField(max_length= 100, blank= False, null= False)
    food_image = models.ImageField(upload_to='food')
    food_price= models.IntegerField(null= False)
    food_category = models.CharField(choices=CATEGORY, max_length= 100)

    def __str__(self):
        return self.food_name   