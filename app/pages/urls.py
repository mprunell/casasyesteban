from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from pages.views import (HomeView, AboutView, WorkView, ConsultancyView,
                         WorkshopsView, ContactView)


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^work$', WorkView.as_view(), name='work'),
    url(r'^consultancy$', ConsultancyView.as_view(), name='consultancy'),
    url(r'^workshops/(?P<wsid>[a-zA-Z0-9-]+)/$', WorkshopsView.as_view(), name='workshops'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)