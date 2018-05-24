from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('<slug:stop_name>/',views.routeSearch,name='routeSearch'),
    path('<slug:stop_name>/',views.routeSearch,name='routeSearch'),
    path('route/<slug:route_name>/',views.routeDisplay,name='routeDisplay'),
    path('route/<slug:start_name>/<slug:stop_name>/',views.journeyDetail,name='journeyDetail'),
]
