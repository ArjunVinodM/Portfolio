from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('', views.index, name="index"),
    # path('contact', views.contact_view, name='contact'),
    path('contact/', contactview.as_view(), name='contact'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)