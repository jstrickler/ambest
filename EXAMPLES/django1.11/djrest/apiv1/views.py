from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from superheroes.models import Superhero, Enemy, Power, City

from .serializers import (
    SuperheroSerializer, PowerSerializer, EnemySerializer, CitySerializer
)

# hero endpoints
@api_view(['GET'])
def superhero_list(request):
    if request.method == 'GET':
        heroes = Superhero.objects.all()
        serialized = SuperheroSerializer(heroes, many=True)
    else:
        pass

    return Response(serialized.data)


@api_view(['GET'])
def superhero_detail(request, pk):
    hero_obj = Superhero.objects.get(pk=pk)
    serialized = SuperheroSerializer(hero_obj)

    return Response(serialized.data)


# power endpoints
@api_view(['GET'])
def power_list(request):
    powers = Superhero.objects.all()
    serialized = SuperheroSerializer(powers, many=True)

    return Response(serialized.data)


@api_view(['GET'])
def power(request, pk):
    power_obj = Power.objects.get(pk=pk)
    serialized = PowerSerializer(power_obj)

    return Response(serialized.data)

# enemy endpoints
class EnemyList(ListAPIView):
    queryset = Enemy.objects.all()
    model = Enemy
    serializer_class = EnemySerializer


class EnemyDetail(RetrieveAPIView):
    queryset = Enemy.objects.all()
    model = Enemy
    serializer_class = EnemySerializer

# city endpoints
