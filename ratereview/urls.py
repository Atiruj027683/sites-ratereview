"""ratereview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.home_redirect),
    url(r'^admin/', admin.site.urls),
    url(r'^sites/', include('sites.urls')),
    url(r'^accounts/', include('accounts.urls')),
<<<<<<< HEAD
    url(r'^books/',include('books.urls')),
=======
    url(r'^recipes/', include('recipes.urls')),
>>>>>>> 9ccd27dbc0c9c42da2bbc62f4c34f031f238d9ee
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
