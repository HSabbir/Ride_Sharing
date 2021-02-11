from django.urls import path
from .views import *

urlpatterns = [
    path('rider/<int:x>/<int:y>/<int:x1>/<int:y1>', rider, name='rider'),
    path('driver/<int:x>/<int:y>',driver,name='driver')
]