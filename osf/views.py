#from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from osf.models import Timeline
from osf.serializers import TimelineSerializer

#this is for the second part.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser


#this is for working with custom queries from django to postgres
from django.db import connection

#working with time
from datetime import date

"""
AGAIN, this was only temporary to show concepts. Good. This is weird. the decorator version shown below is soooooooo
much more normal.


class JSONResponse(HttpResponse):

    An HttpResponse that renders its content into JSON.

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def timeline_list(request):

    List all code snippets, or create a new timeline object.

    if request.method == 'GET':
        timelines = Timeline.objects.all()
        serializer = TimelineSerializer(timelines, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TimelineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def timeline_detail(request, pk):

    Retrieve, update or delete a code timeline.

    try:
        timeline = Timeline.objects.get(pk=pk)
    except Timeline.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TimelineSerializer(timeline)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TimelineSerializer(timeline, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        timeline.delete()
        return HttpResponse(status=204)
"""



#the big thing here is that the HttpRequest and HttpResonse things are old. They are dumb. Django REST has made wrappers
#for them. use the wrapper!

#appropriate curl command is for POST
#curl --header "Content-Type: application/json" -d '{"title":"xyz","users":"xyzsdf", "wiki":"weeeee"}' http://127.0.0.1:8000/timeline/


"""
#@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def create_new_project(request, format=None):

    if request.method == 'GET':
        timelines = Timeline.objects.all()
        serializer = TimelineSerializer(timelines, many=True)
        return Response(serializer.data)

        #1st attempt at custom query from postgres via django
        #cursor = connection.cursor()
        #cursor.execute("select f.title, f.author, f.wiki from get_historical_timeline(1,$) as f", h)
        #print h
        #return Response(cursor.fetchone())



    elif request.method == 'POST':
        serializer = TimelineSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def timeline_detail(request, pk, format=None):

    try:
        timeline = Timeline.objects.get(pk=pk)
    except Timeline.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TimelineSerializer(timeline)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TimelineSerializer(timeline, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        timeline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #print version
    #if h!=0:
    #    version=h
    cursor = connection.cursor()
    #print request.GET
    d = date.today()
    if(request.GET['h']):
        url_date = request.GET['h'].split("-")
        print url_date
        d=date(int(url_date[0]), int(url_date[1]),int(url_date[2]))
    print d
    sql_cmd = "select f.title, f.author, f.wiki from get_historical_timeline({},\'{}\'::timestamp) as f".format(int(pk), d)
    cursor.execute(sql_cmd)
    return Response(cursor.fetchone())
"""
@api_view(['POST'])
def create_new_project(request, format=None):

    if request.method == 'POST':
        serializer = TimelineSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def project_detail(request, format=None):

    if request.method=="GET":
        cursor = connection.cursor()
        d = date.today()
        if 'date' in request.GET and request.GET['date']:
            url_date = request.GET['date'].split("-")
            d=date(month=int(url_date[0]), day=int(url_date[1]),year=int(url_date[2])) # format is to have
        if 'project_id' not in request.GET or not request.GET['project_id']:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        sql_cmd = "select f.title, f.author, f.wiki from get_historical_timeline({},\'{}\'::timestamp) as f".format(int(request.GET['project_id']), d)
        cursor.execute(sql_cmd)
        return Response(cursor.fetchone())
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_project(request):
    if request.method=="PUT":
        serializer = TimelineSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)
