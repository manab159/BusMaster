from django.shortcuts import render
from busMaster.models import *
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    #return HttpResponse(template.render(context, request))
    return render(request, 'busMaster/index.html')
#Takes the Stop Name as the input and displays the Route Name on which it lies

def routeSearch(request):
    if request.method == 'POST':
        #form = NameForm(request.POST)
        stop_name=request.POST['stopName']
        #stop_name=form.stopName
        routeName=""
        stopId=stopMaster.objects.get(sname__iexact=stop_name)
        routeId=routeStop.objects.select_related().filter(stop_id=stopId.sid)
        routeName=routeMaster.objects.select_related().filter(routestop__stop_id=stopId.sid)
        return HttpResponse(routeName)
#Takes the Route Name and displays the stops that that lie on that route
def routeDisplay(request):
    if request.method == 'POST':
        route_name=request.POST['routeName']
        stop_name=""
        routeId=routeMaster.objects.get(rname__iexact=route_name)
        stopId=routeStop.objects.filter(route_id=routeId.rid).values_list('stop_id',flat=True)
        for x in stopId:
            stop_name+='  '.join(stopMaster.objects.filter(sid=x).values_list('sname',flat=True))+"   "
        return HttpResponse(stop_name)
#Takes two Stops and suggests the Possible Routes Between the given Stops
def journeyDetail(request):
    if request.method == 'POST':
        start_name=request.POST['stopName1']
        stop_name=request.POST['stopName2']
        stop_list=[]  
        stopList="" 
        linkStop=[]
        link=[]
        value=""
        start_num=stopMaster.objects.get(sname__iexact=start_name).sid
        stop_num=stopMaster.objects.get(sname__iexact=stop_name).sid
        start=routeStop.objects.filter(stop_id=start_num).values_list('route_id',flat=True)
        end=routeStop.objects.filter(stop_id=stop_num).values_list('route_id',flat=True)
        route=list(set(start) & set(end))
        if route==[]:
            linkStop=stopMaster.objects.filter(routestop__route_id__in=end).filter(routestop__route_id__in=start).values_list('sid',flat=True)[0]
            link=routeMaster.objects.filter(routestop__stop_id=linkStop).values_list('rid',flat=True)[0]
            value+=" "+lineRouteStop(start,routeStop.objects.filter(stop_id=linkStop).values_list('route_id',flat=True),start_num,linkStop)+" "
            value+=" "+lineRouteStop(routeMaster.objects.filter(routestop__stop_id=linkStop).values_list('rid',flat=True),end,linkStop,stop_num)
        else:
            value=lineRouteStop(start,end,start_num,stop_num)   
        return HttpResponse(value)


        # value=""
        # route1=routeStop.objects.filter(stop_id=stopMaster.objects.get(sname__iexact=start_name).sid).values_list('route_id',flat=True)
        # route2=routeStop.objects.filter(stop_id=stopMaster.objects.get(sname__iexact=stop_name).sid).values_list('route_id',flat=True)
        # route12=list(set(route1) & set(route2))
        # if len(route12)==0:
        #     mergeStopId=stopMaster.objects.select_related().filter(routestop__route_id__in=route1).filter(routestop__route_id__in=route2).distinct().values_list('sid',flat=True)
        #     for x in mergeStopId:
        #         value+=" "+lineRouteStop(route1,routeStop.objects.filter(stop_id=x).values_list('route_id',flat=True),stopMaster.objects.filter(sname=start_name).values_list('sid',flat=True),x)
        #         value+=" "+lineRouteStop(routeStop.objects.filter(stop_id=x).values_list('route_id',flat=True),route2,x,stopMaster.objects.get(sname=stop_name).sid)
        #     return HttpResponse(value)


#Function to return the stops between two given Stops on a particular Route
def lineRouteStop(start,end,start_num,stop_num):
    stopName=""
    route=list(set(start) & set(end))
    if len(route)==0:
        return ""
    else:
        for x in route:
            start1=routeStop.objects.get(route_id=x,stop_id=start_num).stopNum
            stop1=routeStop.objects.get(route_id=x,stop_id=stop_num).stopNum

            flag=0
            if start1>stop1:
                temp=start1
                start1=stop1
                stop1=temp
                flag=1
            stop_list=stopMaster.objects.filter(routestop__stopNum__range=(start1,stop1),routestop__route_id=x).values_list('sname',flat=True)
            if flag==1:
                stop_list = stop_list.order_by('-sid')
            stopName+=' '+' - '.join(stop_list)+" ---- "+routeMaster.objects.get(rid=x).rname+"</br>"           
    return stopName

@login_required(login_url='/admin')
def displayRoute(request):
    print(dir(request))
    print(request.user)

    return render(request, 'busMaster/RouteSearch.html')

def displayStop(request):
    return render(request, 'busMaster/stopSearch.html')   

def searchRoute(request):
    return render(request, 'busMaster/Routes.html')    