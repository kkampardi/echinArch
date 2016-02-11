from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = [
        url(r'^$', views.portfolio_list, name='portfolio_list'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
