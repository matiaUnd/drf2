from rest_framework import serializers 
from .models import Proyecto

class ProyectoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Proyecto
        fields= ('id', 'title', 'description', 'tecnology', 'created_at')
        read_only_feilds= ('created_at',)