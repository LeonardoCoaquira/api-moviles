from django.urls import path , include

from .views import *
from . import views
from  rest_framework import routers

router = routers.DefaultRouter()
router.register('zona' , ZonaViewSet)
router.register('tipo_aula' , TipoAulaViewSet)
router.register('aula' , AulaViewSet)

router.register('persona' , PersonaViewSet)

router.register('usuarios' , UserViewSet)

router.register('horario' ,HorarioViewSet , basename='horario')
router.register('horario_persona' ,HorarioPersonaViewSet)







urlpatterns = [
 
    #path('',views.IndexView.as_view(),name='index'),
    path('' , include(router.urls)),

   #path('horario', views.HorarioViewSet.as_view()),
    #path('horario_persona', views.HorarioProfesorViewSet.as_view()),

      #Horario
      path('horario',views.HorarioView.as_view(),name='producto'),
    path('horario/<int:horario_id>',views.HorarioDetailView.as_view()),

    #HorarioPersona
      path('horario_persona',views.HorarioPersonaView.as_view(),name='producto'),
    path('horario_persona/<int:horario_id>',views.HorarioPersonaDetailView.as_view()),
]
