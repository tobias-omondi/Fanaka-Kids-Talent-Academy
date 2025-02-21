import qrcode.constants
from myapp.serializers import studentsSerializer , imagesSerializer , VideosSerializer , BlogSerializer , EventsSerializer , MessageSerializer , RankingSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Student , Image_Gallery , Videos_Gallery , Blog , Events , Message , Ranking
import qrcode
from io import BytesIO
from django.http import HttpResponse

@api_view(['GET'])
def homepage(request):
    return Response({'message': 'Welcome to fanaka kids talent academy'})


@api_view(['GET','POST','DELETE'])
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
    
    elif request.method == 'DELETE':
        student_id = request.data.get('id')  
    try:
        student = Student.objects.get(id=student_id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    



@api_view(['GET','POST', 'DELETE'])
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
    
    elif request.method == 'DELETE':
        image_id = request.data.get('id')
    try:
        images = Image_Gallery.objects.get(id = image_id)
        images.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    except images.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    



@api_view(['GET', 'POST', 'DELETE'])
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
    
    elif request.method == 'DELETE':
        videos_id = request.data.get('id')  # Get the ID from the request data
    try:
            video = Videos_Gallery.objects.get(id=videos_id)  
            video.delete()  # Delete the object
            return Response(status=status.HTTP_204_NO_CONTENT)  
    except Videos_Gallery.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
    



@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def blog(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()  
        serializer = BlogSerializer(blogs, many=True)  
        return Response(serializer.data) 

    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    elif request.method == 'DELETE':
        blog_post_id = request.data.get('id')  
        try:
            blog_post = Blog.objects.get(id=blog_post_id)  
            blog_post.delete()  # Delete the object
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  

    elif request.method == 'PUT':
        blog_post_id = request.data.get('id') 
        try:
            blog_post = Blog.objects.get(id=blog_post_id) 
            serializer = BlogSerializer(blog_post, data=request.data) 
            if serializer.is_valid():  
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  
    
    
    
    
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def events(request):
    if request.method == 'GET':
        events = Events.objects.all()  
        serializer = EventsSerializer(events, many=True)  
        return Response(serializer.data)  

    elif request.method == 'POST':
        serializer = EventsSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    elif request.method == 'DELETE':
        event_id = request.data.get('id')  
        try:
            event = Events.objects.get(id=event_id)  
            event.delete()  
            return Response(status=status.HTTP_204_NO_CONTENT)  
        except Events.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 

    elif request.method == 'PUT':
        event_id = request.data.get('id')  
        try:
            event = Events.objects.get(id=event_id) 
            serializer = EventsSerializer(event, data=request.data) 
            if serializer.is_valid(): 
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        except Events.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Return not found if the object does not exist
            

@api_view(['GET', 'POST'])
def message (request):
    if request.method == 'GET':
       messages = Message.objects.all()
       serializer = MessageSerializer(messages , many = True)
       return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer = MessageSerializer(data = request.data)
        if serializer.is_valid(): serializer.save()
        return Response (serializer.data , status=status.HTTP_201_CREATED)
    return Response (serializer.data , status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def ranking (request):
    if request.method == 'GET':
        rankings = Ranking.objects.all()
        serializer = RankingSerializer(rankings , many = True)
        return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer = MessageSerializer (data = request.data)
        if serializer.is_valid():serializer.save()
        return Response (serializer.data , status=status.HTTP_201_CREATED)
    return Response (serializer.data , status=status.HTTP_400_BAD_REQUEST)



# qrcode for the website

def qr_code(request):
    data = "/"  # the link to our website
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Serve the QR code as an image response
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

#