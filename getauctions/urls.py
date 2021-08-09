from django.urls import path
from . import views

app_name = 'getauctions'

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('search/', views.SearchResultsView.as_view(), name = 'search_results'),
    path('<str:identificador>', views.Index)
    
]