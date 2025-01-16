from myapp.serializers import studentsSerializer , imagesSerializer , VideosSerializer , BlogSerializer , EventsSerializer , MessageSerializer , RankingSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Student , Image_Gallery , Videos_Gallery , Blog , Events , Message , Ranking

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

@api_view(['GET', 'POST'])
def video_gallery(request):
    if request.method == 'GET':
        videos = Videos_Gallery.objects.all() #fetching videos table
        serializer = VideosSerializer (videos , many = True)
        return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer = VideosSerializer (data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def blog (request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs , many = True)
        return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def events (request):
    if request.method == 'GET':
        events = Events.objects.all()
        serializer = EventsSerializer(events , many = True)
        return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer = EventsSerializer(data = request.data)
        if serializer.is_valid():serializer.save
        return Response (serializer.data ,status=status.HTTP_201_CREATED)
    return Response (serializer.data , status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['GET', 'POST'])
def message (request):
    if request.method == 'GET':
       messages = Message.objects.all()
       serializer = MessageSerializer(messages , many = True)
       return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer = MessageSerializer(data = request.data)
        if serializer.is_valid:serializer.save()
        return Response (serializer.data , status=status.HTTP_201_CREATED)
    return Response (serializer.data , status=status.HTTP_400_BAD_REQUEST)

    return Response('message')

@api_view(['GET', 'POST'])
def ranking (request):
    if request.method == 'GET':
        rankings = Ranking.objects.all()
        serializer = RankingSerializer(rankings , many = True)
        return Response (serializer.data)
    
    elif request.method == 'POST':
        serializers = MessageSerializer (data = request.data)
        if serializer.is_valid():serializer.save()
        return Response (serializer.data , status=status.HTTP_201_CREATED)
    return Response (serializer.data , status=status.HTTP_400_BAD_REQUEST)
