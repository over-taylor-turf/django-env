from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    kitchenLocation = models.CharField(max_length=100)
    amountInStorage = models.IntegerField(blank=True)

    def __str__(self):
            return f"{self.name} {self.kitchenLocation} {self.amountInStorage}"
    
    # def as_dict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'kitchenLocation': self.kitchenLocation,
    #         'amountInStorage': self.amountInStorage
    #     }


# Create Food  model with name string, kitchenLocation string, amountInStorage integer and _str_ that returns the name, location and amount in storage as a string