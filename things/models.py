from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        unique=True,
        blank=False,
        max_length=30
    )

    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(validators=[
        MinValueValidator(1, "Value cannot be more than 0"),
        MaxValueValidator(100, "Value cannot be less than 100"),
    ])
