from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.Login,name = 'login'),
    path('',views.home,name = 'home'),
    path('upload/',views.upload,name='upload_file'),
    path('logout/',views.Logout,name='logout'),
    path('<int:id>/',views.f_delete,name='delete')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)