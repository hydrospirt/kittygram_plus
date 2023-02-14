from rest_framework import serializers

from cats.models import Cat


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year')