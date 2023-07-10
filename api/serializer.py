from .models import *
from rest_framework import serializers


class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = '__all__'

class TipoAulaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoAula
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):
    #zona = ZonaSerializer(many=True ,  read_only=True , source='zona_set')
    #tipo_aula= TipoAulaSerializer(read_only=True )
    class Meta:
        model = Aula
        fields = '__all__'
        #fields = ('id' , 'descripcion','estado','zona','tipo_aula')
    


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'


class HorarioPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioPersona
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'usuario', 'clave', 'estado')
