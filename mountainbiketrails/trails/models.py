from django.db import models

class Trail(models.Model):
    name = models.CharField(max_length=200)
    length = models.DecimalField(default=0.1, decimal_places=1, max_digits=3)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    visited_on = models.DateField()
    difficulty_level = models.IntegerField(default=0)
    my_rating = models.IntegerField(default=0)
    top_ten = models.BooleanField(default=False)

    def __str__(self):
        return f"Name: {self.name}, Location: {self.city}, {self.state}, {self.country}\nLength: {self.length}"
