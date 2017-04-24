from corecms.views.admin_form_generator import GenerateFormSendView
from corecms.views.site import MediaView, SearchView, TagResultView, ContactFormView
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from cms.views import GallerySetGlobalView
from website.views.site import ContentItemDetailView

urlpatterns = [
    url(r'^admin/cms/gallery/set-global/$', GallerySetGlobalView.as_view()),
    url(r'^admin/cms/', include('corecms.urls.admin', namespace='admin-corecms')),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next': '/'}, name="logout-url"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('website.urls.site', namespace='website')),
    url(r'^contact-form/$', ContactFormView.as_view(), name='corecms.contact-form'),
    url(r'^contact-form/send/(?P<form_id>\d+)/$', GenerateFormSendView.as_view(), name='corecms.formgen-send'),
    url(r'^tagi/(?P<tag>[\w-]+)/$', TagResultView.as_view(), name='corecms.tags.result'),
    url(r'^szukaj/$', SearchView.as_view(), name='search'),
    # url(r'^media/upload/(?P<hierarchy>[\-\/\w]+)/(?P<file_name>.*)$', MediaView.as_view()),
    url(r'^media/upload/(?P<hierarchy>.*)$', MediaView.as_view()),
    url(r'^(?P<hierarchy>[\-\/\w]+)/$', ContentItemDetailView.as_view(), name='content.detail'),
    url(r'^', include('corecms.urls.site', namespace='corecms')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

