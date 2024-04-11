from django.urls import path
from app.views import *
#from app import views (we can also write it as this and replave app with .)

urlpatterns = [
    path('', home, name="job_home"), #but we have to put views.hello instead of hello
    path('hello/', hello, name="hello"),
    path('job/<int:id>', job_detail, name="job_detail"),
]