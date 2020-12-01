from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vote/(?P<factory_id>[0-9a-f-]+)/$',views.voteview),
    url(r'^vote/(?P<factory_id>[0-9a-f-]+)/continue/$',views.votecontinueview),
    path('conduct/',views.conductvoteview)
]