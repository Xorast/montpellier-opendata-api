from django.db.models import Model, CharField, FloatField, ForeignKey, \
                             IntegerField, DateTimeField, DurationField, \
                             PROTECT, CASCADE


class TransportMode(Model):
    mode = CharField(max_length=20, blank=True, null=True)
    code = IntegerField(primary_key=True)

    def __str__(self):
        return self.mode


class Line(Model):
    route_short_name = CharField(primary_key=True, max_length=50)
    route_long_name = CharField(max_length=200, blank=True, null=True)
    transport_mode = ForeignKey('TransportMode', on_delete=CASCADE)

    def __str__(self):
        return self.route_short_name


class Stop(Model):
    name = CharField(max_length=50, blank=True, null=True)
    code = CharField(primary_key=True, max_length=20)
    stop_id = CharField(max_length=20)
    lat = FloatField(blank=True, null=True)
    lon = FloatField(blank=True, null=True)
    location_type = IntegerField(blank=True, null=True)

    def __str__(self):
        return self.code


class Route(Model):

    line = ForeignKey('Line', related_name='routes', on_delete=CASCADE, null=False)
    headsign = CharField(max_length=50, blank=True, null=True)
    destination_stop = ForeignKey('Stop', on_delete=CASCADE, null=True)
    direction_code = IntegerField(null=False, blank=False)
    route = CharField(primary_key=True, max_length=50, default='default')

    def __str__(self):
        return f"{self.line} - {self.headsign} ({self.direction_code})"

    class Meta:
        unique_together = ('line', 'direction_code')
 
    def save(self, *args, **kwargs):
        self.route = '-'.join([str(self.line), str(self.direction_code)])
        super().save(*args, **kwargs)

class Course(Model):
    route = ForeignKey('Route', on_delete=CASCADE)
    code = CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.code


class PassingTime(Model):
    stop = ForeignKey('Stop', related_name='stops', on_delete=CASCADE)
    course = ForeignKey('Course', related_name='stops', on_delete=CASCADE)
    time_departure = DateTimeField(blank=False, null=False)
    time_delay = DurationField(default=0, null=True)
    passingtime = CharField(primary_key=True, max_length=50)

    class Meta:
            unique_together = ('stop', 'course')

    def __str__(self):
        return f"{self.stop.code} - Line {self.course.route.line.route_short_name} ({str(self.course.route.direction_code)})"

    def save(self, *args, **kwargs):
        self.passingtime = '-'.join([str(self.stop), str(self.course)])
        super().save(*args, **kwargs)
