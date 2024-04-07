from django.urls import path
from app.views import *
#from app import views (we can also write it as this and replave app with .)

urlpatterns = [
    path('', home), #but we have to put views.hello instead of hello
    path('job/<int:id>', job_detail),
]