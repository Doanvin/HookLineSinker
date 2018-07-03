from .views import ReviewGetView

from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ReviewGetView.as_view(), name='get')
]
