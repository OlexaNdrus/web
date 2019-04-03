"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url,include
from qa.views import test,index,popular,question,ask,signup,login_view
from ask.views import found, not_found, init25

from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    url(r'^$', index),
    url(r'^popular/.*$', popular),
    url(r'^ask/.*$', ask),
    url(r'^signup/.*$', signup),
    url(r'^login/.*$', login_view),
    url(r'^new/.*$', found),
    url(r'^question/', include('qa.urls')),


    url(r'^', not_found),
]

