from django.views import *
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns =[  path('',views.load_homepage,name='load_homepage'),
                path('load_bease',views.load_bease,name='load_bease'),
                path('load_mobile',views.load_mobile,name='load_mobile'),
                path('load_csm',views.load_csm,name='load_csm'),
                path('sending_mail',views.sending_mail,name='sending_mail'),


  ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)