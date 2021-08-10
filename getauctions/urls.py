from django.urls import path
from . import views

app_name = 'getauctions'

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('search/', views.SearchResultsView.as_view(), name = 'search_results'),
    path('auctions/', views.AuctionInfoList.as_view()),
    path('auctions/int:<pk>', views.AuctionInfoDetail.as_view())
]