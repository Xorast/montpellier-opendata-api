from rest_framework import serializers
from .models import TransportMode, Line, Stop, \
                    Route, Course, PassingTime


class StopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stop
        fields = ['name', 'code', 'stop_id', 'lat', 'lon']


class TransportModeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportMode
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = '__all__'
        

class RouteSerializer(serializers.ModelSerializer):

    route = serializers.CharField(read_only=True)

    class Meta:
        model = Route
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class PassingTimeSerializer(serializers.ModelSerializer):
    
    passingtime = serializers.CharField(read_only=True)
    
    class Meta:
        model = PassingTime
        fields = '__all__'
