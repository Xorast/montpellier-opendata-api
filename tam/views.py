from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import generics

from .models import TransportMode, Line, Stop, \
                    Route, Course, PassingTime
from .serializers import StopSerializer, TransportModeSerializer, \
                         LineSerializer, PassingTimeSerializer, \
                         CourseSerializer, RouteSerializer



def landing_page(request):
    return HttpResponse('TAM LANDING PAGE')


@api_view(['GET', 'POST'])
def stops_list(request):
    """
    List all stops.
    """
    if request.method == 'GET':
        stops = Stop.objects.all()
        serializer = StopSerializer(stops, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = Stop(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def transportmodes_list(request):
    """
    List all transportmodes.
    """
    if request.method == 'GET':
        transportmodes = TransportMode.objects.all()
        serializer = TransportmodeSerializer(transportmodes, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def lines_list(request):
    """
    List all lines.
    """
    if request.method == 'GET':
        lines = Line.objects.all()
        serializer = LineSerializer(lines, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def passingtimes_list(request):
    """
    List all passing times.
    """
    if request.method == 'GET':
        passingtimes = PassingTime.objects.all()
        serializer = PassingTimeSerializer(passingtimes, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PassingTimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def courses_list(request):
    """
    List all courses.
    """
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def routes_list(request):
    """
    List all routes.
    """
    if request.method == 'GET':
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def stop_detail(request, pk, format=None):
    """
    Retrieve, update or delete stop.
    """
    try:
        stop = Stop.objects.get(pk=pk)
    except Stop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StopSerializer(stop)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StopSerializer(instance=stop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        stop.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def transportmode_detail(request, pk, format=None):
    """
    Retrieve, update or delete a transport mode.
    """
    try:
        transportmode = TransportMode.objects.get(pk=pk)
    except TransportMode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TransportModeSerializer(transportmode)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TransportModeSerializer(instance=transportmode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        transportmode.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def line_detail(request, pk, format=None):
    """
    Retrieve, update or delete a line.
    """
    try:
        line = Line.objects.get(pk=pk)
    except Line.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LineSerializer(line)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = LineSerializer(instance=line, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        line.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT'])
def passingtime_detail(request, pk, format=None):
    """
    Retrieve, update or delete a passing time.
    """
    try:
        passingtime = PassingTime.objects.get(pk=pk)
    except PassingTime.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PassingTimeSerializer(passingtime)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PassingTimeSerializer(instance=passingtime, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        passingtime.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def course_detail(request, pk, format=None):
    """
    Retrieve, update or delete course.
    """
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CourseSerializer(instance=course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        course.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def route_detail(request, pk, format=None):
    """
    Retrieve, update or delete a route.
    """
    try:
        route = Route.objects.get(pk=pk)
    except Route.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RouteSerializer(route)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = RouteSerializer(instance=route, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        route.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
