from django.contrib import admin
from .models import TransportMode, Line, Stop, Route, Course, PassingTime


class StopAdmin(admin.ModelAdmin):
    ordering = ('code',)


class PassingTimeAdmin(admin.ModelAdmin):
    ordering = ('time_departure',)
    readonly_fields = ['passingtime']


admin.site.register(TransportMode)
admin.site.register(Line)
admin.site.register(Stop, StopAdmin)
admin.site.register(Route)
admin.site.register(Course)
admin.site.register(PassingTime, PassingTimeAdmin)
