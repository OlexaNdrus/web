from django.conf.urls import url
from ask.qa.views import test

urlpatterns = [
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test),
    url(r'^(?P<num>\d+)/$', test),

]
