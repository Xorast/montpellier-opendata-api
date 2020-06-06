from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page),
    path('stops/', views.stops_list),
    path('stops/<str:pk>/', views.stop_detail),
    path('transportmodes/', views.transportmodes_list),
    path('transportmodes/<str:pk>/', views.transportmode_detail),
    path('lines', views.lines_list),
    path('lines/<str:pk>/', views.line_detail),
    path('passingtimes/', views.passingtimes_list),
    path('passingtimes/<str:pk>/', views.passingtime_detail),
    path('courses/', views.courses_list),
    path('courses/<str:pk>/', views.course_detail),
    path('routes/', views.routes_list),
    path('routes/<str:pk>/', views.route_detail),
]
