from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Trail(models.Model):
    name = models.CharField(max_length=200)
    length = models.DecimalField(default=0.1, decimal_places=1, max_digits=3, validators=[MinValueValidator(0.0)])
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    visited_on = models.DateField(null=True, blank=True)
    difficulty_level = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    my_rating = models.PositiveIntegerField(default=0, blank=True, null=True, validators=[MaxValueValidator(5)])
    top_ten = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"Name: {self.name} - Location: {self.city}, {self.state}, {self.country} - Length: {self.length} miles"