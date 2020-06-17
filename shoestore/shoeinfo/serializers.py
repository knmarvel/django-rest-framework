from django.contrib.auth.models import User, Group
from .models import Manufacturer, Shoe, ShoeColor, ShoeType
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['url', 'name', 'website']

class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'url',
            'size',
            'brand-name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
            ]

class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['url', 'style']


class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['url', 'color_name']
