from braces.views._access import StaffuserRequiredMixin
from braces.views._forms import CsrfExemptMixin
from corecms.models.gallery import Gallery
from django.http.response import JsonResponse
from django.views.generic.base import View

from cms.models import GalleryDistinction


class GallerySetGlobalView(CsrfExemptMixin, StaffuserRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        gallery = Gallery.objects.get(pk=request.POST["gallery_id"])

        print request.POST.get('set', u"1"), type(request.POST.get('set', u"1"))

        set_global = request.POST.get('set', u"1") == u"1"

        print set_global

        if set_global:
            GalleryDistinction.objects.get_or_create(gallery=gallery, defaults=dict(in_global=True))
        else:
            print 'delete'
            GalleryDistinction.objects.filter(gallery=gallery).delete()
        response = {
            "active": 1 if set_global else 0
        }
        return JsonResponse(response)
