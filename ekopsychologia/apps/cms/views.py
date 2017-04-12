from braces.views._access import StaffuserRequiredMixin
from braces.views._forms import CsrfExemptMixin
from corecms.models.gallery import Gallery
from django.http.response import JsonResponse
from django.views.generic.base import View

from cms.models import GalleryDistinction


class GallerySetGlobalView(CsrfExemptMixin, StaffuserRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        gallery = Gallery.objects.get(pk=request.POST["gallery_id"])
        if request.POST.get('set'):
            GalleryDistinction.objects.get_or_create(gallery=gallery, defaults=dict(in_global=True))
        else:
            GalleryDistinction.objects.filter(gallery=gallery).delete()
        response = {
            "active": request.POST.get('set', True)
        }
        return JsonResponse(response)
