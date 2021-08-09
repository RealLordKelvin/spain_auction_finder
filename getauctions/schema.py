'''

import graphene
from graphene_django import DjangoObjectType
from .models import AuctionInfo


class AuctionInfoType(DjangoObjectType):
    class Meta: 
        model = AuctionInfo
        
        fields = (
            'identificador',
            'tipo_subasta',
            'fecha_inicio',
            'fecha_conclusion',
            'tasacion', 
            'puja_minima',
            'importe_deposito', 
            'cantidad_reclamada',
            'localidad',
            'descripcion',
        )  
        
class Query(graphene.ObjectType):
    
    auctioninfos = graphene.List(AuctionInfoType)

    def resolve_auctioninfos(root, info, **kwargs):
        # Querying a list
        return AuctionInfo.objects.all()

'''
class AuctionInfoInput(graphene.InputObjectType):

    identificador = graphene.String()
    tipo_subasta = graphene.String()
    fecha_inicio = graphene.String()
    fecha_conclusion = graphene.String()
    tasacion = graphene.String()
    puja_minima = graphene.String()
    importe_deposito = graphene.String()
    cantidad_reclamada = graphene.String()
    localidad = graphene.String()
    descripcion = graphene.String()


class CreateAuctionInfo(graphene.Mutation):
    class Arguments:
        input = AuctionInfoInput(required = True)

    auction = graphene.Field(AuctionInfoType)
        
    @classmethod
    def mutate(cls, root, info, input):
        auction = auctioninfo()
        auction.identificador = input.identificador
        auction.tipo_subasta = input.tipo_subasta
        auction.fecha_inicio = input.fecha_inicio
        auction.fecha_conclusion = input.fecha_conclusion
        auction.tasacion = input.tasacion
        auction.puja_minima = input.puja_minima
        auction.importe_deposito = input.importe_deposito
        auction.cantidad_reclamada = input.tasacion
        auction.localidad = input.puja_minima
        auction.descripcion = input.importe_deposito
        auction.save()
        return CreateAuctionInfo(auction = auction)

class UpdateAuctionInfo(graphene.Mutation):
    class Arguments:
        input = AuctionInfoInput(required=True)
        #id = graphene.ID()

    auction = graphene.Field(AuctionInfoType)
        
    @classmethod
    def mutate(cls, root, info, input, id):
        auction = Product.objects.get(pk=id)
        auction.identificador = input.identificador
        auction.tipo_subasta = input.tipo_subasta
        auction.fecha_inicio = input.fecha_inicio
        auction.fecha_conclusion = input.fecha_conclusion
        auction.tasacion = input.tasacion
        auction.puja_minima = input.puja_minima
        auction.importe_deposito = input.importe_deposito
        auction.cantidad_reclamada = input.tasacion
        auction.localidad = input.puja_minima
        auction.descripcion = input.importe_deposito
        auction.save()
        return UpdateAuctionInfo(auction = auction)


class Mutation(graphene.ObjectType):
    
    create_auction = CreateAuctionInfo.Field()
    update_auction = UpdateAuctionInfo.Field()
'''
schema = graphene.Schema(query=Query)#, mutation=Mutation)
'''