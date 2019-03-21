from django.conf.urls import url, include
from django.contrib import admin

from qa.views import test

urlpatterns = [
    url(r'^$', test),
    url(r'^blablabla/.*$', test),
    url(r'^popular/.*$', test),
    url(r'^ask/.*$', test),
    url(r'^signup/.*$', test),
    url(r'^login/.*$', test),
    url(r'^new/.*$', test),
    url(r'^question/(?P<question_id>[0-9]+)/$', test),
]