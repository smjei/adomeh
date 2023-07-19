from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='leumas-index'),
    path('blog', views.blog, name='leumas-blog'),
    path('blogpost', views.blogpost, name='leumas-blogpost'),
    path('sam404', views.sam404, name='leumas-sam404'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
