"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:_
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
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from first_app import views
urlpatterns = [
    url(r'^$',views.maan,name='maan'),
    url(r'^post_detail/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^',include('first_app.urls',namespace='first_app')),
    # url(r'^help/',views.help,name='help'),
    # url(r'^forms/', views.forms_view, name='forms'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', views.user_logout,name='logout'),
    url(r'^Announcement/', views.index, name='index'),
    url(r'^special/', views.special,name='special')
] + static(settings.MEDIA_URL, document_root=settings.MEDIAFILES_DIRS)
