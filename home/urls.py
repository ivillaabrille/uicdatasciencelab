from django.conf.urls import url
from . import views

app_name= 'home'

urlpatterns = [
    # /
    url(r'^$', views.IndexView, name='index'),

    # /contact/
    url(r'^connect/$', views.ConnectView, name='connect'),

    # /success/
    url(r'^success/$', views.SuccessView, name='success'),

    # /team/
    url(r'^team/$', views.TeamView, name='team'),

    # /news/
    url(r'^news/$', views.NewsView.as_view(), name='news'),

    # /research/
    url(r'^research/$', views.ResearchView.as_view(), name='research'),

    # /news/1/
    url(r'^news/(?P<pk>[0-9]+)/$', views.NewsDetailView.as_view(), name='newsdetail'),

    # /research/1/
    url(r'^research/(?P<pk>[0-9]+)/$', views.ResearchDetailView.as_view(), name='researchdetail'),

]
