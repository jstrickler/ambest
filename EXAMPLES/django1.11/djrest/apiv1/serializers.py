#!/usr/bin/env python
# (c) 2017 CJ Associates
#
from rest_framework import serializers
from superheroes.models import Superhero, City, Power, Enemy

class SuperheroSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    enemies = serializers.StringRelatedField(many=True)
    powers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Superhero
        fields = (
            'id', 'name', 'secret_identity', 'real_name', 'city', 'enemies',
            'powers'
        )


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('name')


class PowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Power
        fields = ('id', 'name', 'description')


class EnemySerializer(serializers.ModelSerializer):
    powers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Enemy
        fields = ('id', 'name', 'powers')

