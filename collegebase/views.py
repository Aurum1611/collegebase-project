from django.http import HttpResponse

def index(req):
    return HttpResponse('<h1>Hey there!</h1>')