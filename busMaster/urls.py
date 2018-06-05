from django.urls import path

from . import views


app_name='busMaster'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<slug:stop_name>/',views.routeSearch,name='routeSearch'),
    #path('<slug:stop_name>/',views.routeSearch,name='routeSearch'),
    path('displayRoute',views.displayRoute,name='displayRoute'),
    path('routeSearch',views.routeSearch,name='routeSearch'),
    path('displayStop',views.displayStop,name='displayStop'),
    path('stopSearch',views.routeDisplay,name='routeDisplay'),
    #path('route/<slug:route_name>/',views.routeDisplay,name='routeDisplay'),
    path('searchRoute',views.searchRoute,name='searchRoute'),
    path('journeyDetail',views.journeyDetail,name='journeyDetail'),
    #path('route/<slug:start_name>/<slug:stop_name>/',views.journeyDetail,name='journeyDetail'),
]
