from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from pages.views import HomeView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)