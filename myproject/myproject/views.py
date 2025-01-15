from django.http import HttpResponse

def homepage(request):
    return HttpResponse('homepage')

def image_gallery (request):
    return HttpResponse('images')


def video_gallery(request):
    return HttpResponse('videos')

def blog (request):
    return HttpResponse('blog')

def events (request):
    return HttpResponse('events')

def ranking (request):
    return HttpResponse('ranking')

def message (request):
    return HttpResponse('message')