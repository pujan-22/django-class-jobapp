import http
from os import execv
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader

# Create your views here.
job_title = [
    '',
    'Job Title 1', 'Job Title 2', 'Job Title 3'
]

job_desc = [
    '','Description 1', 'Description 2', 'Description 3'
]

class TempClass:
    a = 10

def hello(request):
    template = loader.get_template('app/hello.html')
    list = ["a value", "second value"]
    temp_class = TempClass()
    context = {"user" : "Pujan", "list" : list, "temp_class" : temp_class}
    return HttpResponse(template.render(context, request))

def home(request):
    job_list = "<ul>"
    for i in job_title:
        job_id = job_title.index(i)
        detail_url = reverse('job_detail', args=(job_id, ))
        job_list += f"<li><a href='{detail_url}'>{i}</a></li>"
    job_list += "</ul>"
    return HttpResponse(f"<h1>Hello World!!!</h1> {job_list}")

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse("job_home"))
        site = f"<h1>{job_title[id]}</h1> {job_desc[id]}"
        return HttpResponse(site)
    except:
        return HttpResponseNotFound("Not Found")