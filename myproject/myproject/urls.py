from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,views.homepage, name = 'homepage'),
    path('images/', views.image_gallery, name='image_gallery'),
    path('videos/', views.video_gallery, name='video_gallery'),
    path('blog/', views.blog, name='blog'),
    path('events/', views.events, name='events'),
    path('ranking/', views.ranking, name='ranking'),
    path('message/', views.message, name='message'),
    # path('api-auth/', include('rest_framework.urls')),
]