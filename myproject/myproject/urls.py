from django.contrib import admin
from django.urls import path , include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('access-panel/', views.admin_login, name='admin-login'),
    path('' ,views.homepage, name = 'homepage'),
    path('students/', views.students, name = 'students'),
    path('images/', views.image_gallery, name='image_gallery'),
    path('images/<int:id>/',views.image_gallery, name = 'image_details'),
    path('videos/', views.video_gallery, name='video_gallery'),
    path('videos/<int:id>/',views.video_gallery, name = 'videos_details'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog, name='blog-detail'),
    path('events/', views.events, name='events'),
    path('events/<int:id>/', views.events, name = 'events-detail' ),
    path('ranking/', views.ranking, name='ranking'),
    path('message/', views.message, name='message'),
    path('api-auth/', include('rest_framework.urls')),
    path('qr-code/', views.qr_code, name='qr_code'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)