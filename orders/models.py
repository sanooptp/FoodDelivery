from django.db import models
from accounts.models import User

from foods.models import Food

class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    food= models.ForeignKey(Food, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add= True)
    price= models.IntegerField(null= False)
    is_placed= models.BooleanField(default= False)
    is_delivered= models.BooleanField(default= False)
    comment= models.CharField(max_length= 500, null= True, blank= True, default= '')

    def __str__(self):
        return self.user, self.food