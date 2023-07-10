from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics

from .models import *
from .serializer import *
from django.http import Http404, JsonResponse
import subprocess
from rest_framework.decorators import api_view

from datetime import date ,datetime
class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo API FINAL'}
        return Response(context)


class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer

class TipoAulaViewSet(viewsets.ModelViewSet):
    queryset = TipoAula.objects.all()
    serializer_class = TipoAulaSerializer


class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class HorarioPersonaViewSet(viewsets.ModelViewSet):
    queryset = HorarioPersona.objects.all()
    serializer_class = HorarioPersonaSerializer


""" class HorarioViewSet(APIView):
    def get(self, request):
        aula = request.GET.get('aula_id')#aula
        queryset = Horario.objects.all()
        if aula:
            queryset = queryset.filter(aula = aula).order_by('hora_inicio')
        serializer = HorarioSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HorarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return Horario.objects.get(pk=pk)
        except Horario.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = HorarioSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=204)

class HorarioProfesorViewSet(APIView):
    def get(self, request):
        horario = request.GET.get('horario_id')
        queryset = HorarioPersona.objects.all()
        if horario:
            queryset = queryset.filter(horario = horario)
        serializer = HorarioPersonaSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HorarioPersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return HorarioPersona.objects.get(pk=pk)
        except HorarioPersona.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = HorarioPersonaSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=204) """
    
class HorarioPersonaView(APIView):
    
    def get(self,request):
        aula = request.GET.get('horario_id')
        persona =  request.GET.get('persona_id')
        print(persona)
        queryset = HorarioPersona.objects.all()
     
        if aula:#filtar por aulas
            queryset = queryset.filter(aula = aula)
        elif persona :#filtra por personas
            queryset = queryset.filter(persona = persona)
            #queryset = Horario.objects.filter(id = persona.persona )
            # Si no se especifican los filtros, devolver todas las horas de inicio y fin
            horarios = []
            for horario_persona in queryset:
                horario = horario_persona.horario
                aula_id = horario_persona.horario.aula.id
                persona_id = horario_persona.persona.id
                zona = horario_persona.horario.aula.zona.nombre
                horarios.append({
                    'id' : horario_persona.id,
                    'horario_inicio': horario.hora_inicio,
                    'horario_fin': horario.hora_final,
                    'aula_id': horario.aula.descripcion,
                    'persona_id': persona_id,
                    'zona': zona,
                    'clave' : horario_persona.password
                    # Agrega otros campos que desees incluir
                })

            return Response(horarios)

        serHorarioPersona = HorarioPersonaSerializer(queryset, many=True)
        return Response(serHorarioPersona.data)


        serHorarioPersona = HorarioPersonaSerializer(queryset,many=True)
        return Response(serHorarioPersona.data)
    
    def post(self,request):
        serHorarioPersona = Horario(data=request.data)
        serHorarioPersona.is_valid(raise_exception=True)
        serHorarioPersona.save()
        
        return Response(serHorarioPersona.data)
    
class HorarioPersonaDetailView(APIView):
    
    def get(self,request,horario_id):
        dataHorarioPersona = HorarioPersona.objects.get(pk=horario_id)
        horario_inicio = dataHorarioPersona.horario.hora_inicio
        horario_final = dataHorarioPersona.horario.hora_final

        response_data = {
            'id': dataHorarioPersona.id,
            'horario_inicio': horario_inicio,
            'horario_fin': horario_final,
            # Agrega otros campos que desees incluir en la respuesta
        }

        return Response(response_data)
    
    def put(self,request,horario_id):
        dataHorarioPersona = HorarioPersona.objects.get(pk=horario_id)
        serHorarioPersona = HorarioPersonaSerializer(dataHorarioPersona,data=request.data)
        serHorarioPersona.is_valid(raise_exception=True)
        serHorarioPersona.save()
        return Response(serHorarioPersona.data)
    
    def delete(self,request,horario_id):
        dataHorarioPersona = HorarioPersona.objects.get(pk=horario_id)
        serHorarioPersona = HorarioPersonaSerializer(dataHorarioPersona)
        dataHorarioPersona.delete()
        return Response(serHorarioPersona.data)







class HorarioView(APIView):
    
    def get(self,request):
        aula = request.GET.get('aula_id')
        horario_id = request.GET.get('horario_id')
        #fecha = request.GET.get('fecha')
        #fecha_actual = str(date.today().strftime("%Y-%m-%d"))
        #fecha_actual = datetime.now().date()
        queryset = Horario.objects.all()

        if aula : 
            queryset = queryset.filter(aula = aula)
        #elif fecha :
        #    queryset = queryset.filter(fecha=fecha_actual)
        serHorario = HorarioSerializer(queryset,many=True)
        return Response(serHorario.data)
        

    def post(self,request):
        serHorario = HorarioSerializer(data=request.data)
        serHorario.is_valid(raise_exception=True)
        serHorario.save()
        
        return Response(serHorario.data)
    
class HorarioDetailView(APIView):
    
    def get(self,request,horario_id):
        dataHorario = Horario.objects.get(pk=horario_id)
        serHorario = HorarioSerializer(dataHorario)
        return Response(serHorario.data)
    
    def put(self,request,horario_id):
        dataHorario = Horario.objects.get(pk=horario_id)
        serHorario = HorarioSerializer(dataHorario,data=request.data)
        serHorario.is_valid(raise_exception=True)
        serHorario.save()
        return Response(serHorario.data)
    
    def delete(self,request,horario_id):
        dataHorario = Horario.objects.get(pk=horario_id)
        serHorario = HorarioSerializer(dataHorario)
        dataHorario.delete()
        return Response(serHorario.data) 


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)