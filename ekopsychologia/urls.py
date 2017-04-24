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
    url(r'^(?P<hierarchy>[\-\/\w]+)/$', ContentItemDetailView.as_view(), name='content.detail'),
    url(r'^', include('corecms.urls.site', namespace='corecms')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

