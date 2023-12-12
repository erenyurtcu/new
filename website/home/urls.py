from django.urls import path
from . import views

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.home),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("<int:pk>/" , views.admin_media_detail, name="postdetail"),
    path("contact", views.contact, name="contact"),
    path("bg-home", views.bgIndex, name="bg-index"),
    path("atolye-iletisim", views.atolye_iletisim, name="atolye-iletisim"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "BETÜL GÜNEY"