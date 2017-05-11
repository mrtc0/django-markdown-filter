from django.conf.urls import url
from app.views import index


urlpatterns = [
    url(r'^$', index, name='index'),
]
