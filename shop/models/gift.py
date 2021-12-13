from django.db import models

# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    amountInStorage = models.IntegerField(blank=True)

    def __str__(self):
            return f"{self.name} {self.type} {self.amountInStorage}"
    
    # def as_dict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'type': self.type,
    #         'amountInStorage': self.amountInStorage
    #     }


# Create Food  model with name string, kitchenLocation string, amountInStorage integer and _str_ that returns the name, location and amount in storage as a string