"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.work.views import home
from apps.contact.views import ContactList

urlpatterns = [
    path("admin/", admin.site.urls),
    # tinymce urls
    path("tinymce/", include("tinymce.urls")),
    # Home page url
    path("", home, name="home"),
    # Work page urls
    path("works/", include("apps.work.urls")),
    # studio urls
    path("studio/", include("apps.studio.urls")),
    # contact page url
    path("contact/", ContactList.as_view(), name="contact_list")
]

# Static and media file urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Change  default site header
admin.site.site_header = "Gaatha administration"
