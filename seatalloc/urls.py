from django.conf.urls import patterns, url
from seatalloc import views

urlpatterns = patterns('',
        url(r'^index$', views.index , name='index'),
        url(r'^detail$',views.add_candidate, name='add_candidate'),
        url(r'^detail/(?P<candidate_roll>\w+)$',views.candidate,name='candidate'),
        url(r'^detail/(?P<candidate_roll>\w+)/add_preference$',views.add_preference,name='add_preference'),
        )
       
