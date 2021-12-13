from django.db import models

# Create your models here.
class Dorm(models.Model):
    name = models.CharField(max_length=100)
    total_capacity = models.IntegerField(blank=True)
    current_capacity = models.IntegerField(blank=True)

    def __str__(self):
            return f"{self.name} has {self.current_capacity} of {self.total_capacity} dorm rooms filled."