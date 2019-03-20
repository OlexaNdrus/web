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

from django.conf.urls import url
from ask.qa.views import test


urlpatterns = [

    url(r'^$', test),

    url(r'^init25/', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^ask/', test),

    url(r'^popular/', test),
    url(r'^new/', test),

    url(r'^admin/', test),
    url(r'^question/', test),

    url(r'^', test),
]
