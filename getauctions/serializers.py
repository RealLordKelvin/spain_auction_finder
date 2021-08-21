from .models import AuctionInfo
from rest_framework import serializers

class AuctionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionInfo
        fields = [
            'pk',
            'timestamp',
            'identificador',
            'direccion',
            'provincia',
            'tipo_subasta',
            'fecha_inicio',
            'fecha_conclusion',
            'tasacion',
            'puja_minima',
            'importe_deposito', 
            'cantidad_reclamada', 
            'codigo_postal',
            'ciudad',
            'correo_electronico',
            'descripcion',
        ]

        extra_kwargs = {
            'descripcion': {'required': False},
            'provincia': {'required': False},
            'puja_minima': {'required': False},

        }
    