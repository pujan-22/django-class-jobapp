import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
job_title = [
    '',
    'Job Title 1', 'Job Title 2', 'Job Title 3'
]

job_desc = [
    '','Description 1', 'Description 2', 'Description 3'
]

def home(request):
    job_list = "<ul>"
    for i in job_title:
        job_id = job_title.index(i)
        job_list += f"<li><a href='job/{job_id}'>{i}</a></li>"
    job_list += "</ul>"
    return HttpResponse(f"<h1>Hello World!!!</h1> {job_list}")

def job_detail(request, id):
    if id == 0:
        return redirect("/")

    site = f"<h1>{job_title[id]}</h1> {job_desc[id]}"
    return HttpResponse(site)