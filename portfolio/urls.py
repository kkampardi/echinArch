from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = [
        url(r'^$', views.portfolio_list, name='portfolio_list'),
        url(r'^project/(?P<pk>[0-9]+)/$', views.portfolio_detail, name='portfolio_detail'),
        url(r'^about$', views.about, name='about'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
