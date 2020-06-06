from django.contrib import admin
from django.urls import path, include
import home, tam

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('tam/', include('tam.urls'))
]
