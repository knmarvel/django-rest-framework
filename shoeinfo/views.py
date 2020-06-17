from rest_framework import viewsets
from shoeinfo.models import (
    Shoe,
    ShoeType,
    ShoeColor,
    Manufacturer
    )
from shoeinfo.serializers import (
    ShoeColorSerializer,
    ShoeTypeSerializer,
    ShoeSerializer,
    ManufacturerSerializer,
)


# Create your views here.
class ShoeViewSet(viewsets.ModelViewSet):
    """
    Views the shoes
    """
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    """
    Views the ShoeColors
    """
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    """
    Views the ShoeTypes
    """
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    Views the Manufacturers
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
