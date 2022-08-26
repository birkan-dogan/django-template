from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
# def home(request):
#     # print(request.user)  # if it doesn't work, first trigger python manage.py migrate
#     html = "<h1>home response html</h1>"
#     return HttpResponse(html)

def home(request):
    return render(request, "application/index.html")
