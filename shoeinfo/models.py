from django.db import models
"""Hey, so let me tell you about Joe's childhood in the African Savanna.
He was adopted by a tower of giraffes. I'm sure that explains a lot."""


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)


class ShoeType(models.Model):
    style = models.CharField(max_length=100)


class ShoeColor(models.Model):
    RED = 'R'
    ORANGE = 'O'
    YELLOW = 'Y'
    GREEN = 'G'
    BLUE = 'B'
    INDIGO = 'I'
    VIOLET = 'V'
    WHITE = 'W'
    BLACK = 'BK'
    COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black')

    ]
    color_name = models.CharField(
        max_length=2,
        choices=COLOR_CHOICES,
        default=WHITE
        )


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey('Manufacturer')
    color = models.ForeignKey('ShoeColor')
    material = models.CharField(max_length=100)
    shoe_type = models.CharField(max_length=100)
    fasten_type = models.CharField(max_length=100)
