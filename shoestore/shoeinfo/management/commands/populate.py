from django.core.management.base import BaseCommand, CommandError
from shoeinfo.models import ShoeType, ShoeColor


class Command(BaseCommand):
    help = 'Populates the shoetype and shoecolor tables'

    def add_arg