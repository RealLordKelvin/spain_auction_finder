from django.shortcuts import render, HttpResponse
from .models import AuctionInfo
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from django.views import generic

'''
def HomePageView(response):
    return render(response, "getauctions/home.html", {})

'''
    #return render(response, "getauctions/search_results.html", {'model': model})

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
            Q(comunidad__icontains=query)
        )
        return object_list