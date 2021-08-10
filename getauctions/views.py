from django.shortcuts import render, HttpResponse
from .models import AuctionInfo
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from django.views import generic

from .serializers import AuctionInfoSerializer
from rest_framework import generics

class AuctionInfoList(generics.ListCreateAPIView):
    queryset = AuctionInfo.objects.all()
    serializer_class = AuctionInfoSerializer
    
class AuctionInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuctionInfo.objects.all()
    serializer_class = AuctionInfoSerializer



def Index(response, identificador):
    model = AuctionInfo.objects.get(identificador=identificador)
    return render(response, 'getauctions/search_results.html', {'model': model})


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = AuctionInfo
    template_name = 'search_results.html'
    #queryset = model.objects.filter(identificador__icontains='SUB-JA-2021-170174')
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = AuctionInfo.objects.filter(
            Q(provincia__icontains=query)
        )
        print(object_list)
        return object_list