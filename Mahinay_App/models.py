from django.db import models


class Food(models.Model):

    CATEGORY_CHOICES = [
        ('Meals', 'Meals'),
        ('Snacks', 'Snacks'),
        ('Drinks', 'Drinks'),
        ('Desserts', 'Desserts'),
    ]

    food_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Meals'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_status = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name