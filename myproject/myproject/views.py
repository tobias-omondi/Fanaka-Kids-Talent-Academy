from myapp.serializers import studentsSerializer , imagesSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Student , Image_Gallery

@api_view(['GET'])
def homepage(request):
    return Response({'message': 'Welcome to fanaka kids talent academy'})

@api_view(['GET','POST'])
def students(request):
    if request.method == 'GET':
        students = Student.objects.all()   # we are initializing our student then serializing to give as unique data of each objects
        serializer = studentsSerializer(students, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = studentsSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def image_gallery (request):
    if request.method == 'GET':
        images = Image_Gallery.objects.all()  # fetching all images data
        serializer = imagesSerializer (images , many = True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = imagesSerializer (data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response('images')


def video_gallery(request):
    return Response('videos')

def blog (request):
    return Response('blog')

def events (request):
    return Response('events')

def ranking (request):
    return Response('ranking')

def message (request):
    return Response('message')