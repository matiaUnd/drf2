from proyecto.models import Proyecto
from rest_framework import viewsets, permissions
from .serializers import ProyectoSerializers

class ProyectViewSet(viewsets.ModelViewSet):
    queryset=Proyecto.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= ProyectoSerializers
    