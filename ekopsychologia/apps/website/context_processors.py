from cms.models import Site


def default(request):
    try:
        site = Site.objects.published().get(slug="projekty")
        return dict(menu_bottom_projects=site.children.published()[:4], menu_bottom_project=site)
    except Site.DoesNotExist:
        return {}
