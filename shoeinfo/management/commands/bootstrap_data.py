from django.core.management.base import BaseCommand
from shoeinfo.models import ShoeType, ShoeColor


class Command(BaseCommand):
    help = 'Populates the shoetype and shoecolor tables'

    def handle(self, *args, **options):
        styles = [
            "sneaker",
            "boot",
            "sandal",
            "dress",
            "other"
        ]
        colors = [
            "R",
            "O",
            "Y",
            "G",
            "B",
            "I",
            "V",
            "W",
            "BK"
        ]
        for style in styles:
            ShoeType.objects.create(style=style)
        for color in colors:
            ShoeColor.objects.create(color_name=color)
