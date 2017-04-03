#coding=utf-8
from django.db import models


class BlockSliderCategory(models.Model):
    identity = models.SlugField(verbose_name='Identyfikator')
    name = models.CharField(verbose_name="Nazwa", max_length=200)

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.identity)

    class Meta:
        app_label = u'blockslider'
        verbose_name = u"Kategoria slidera"
        verbose_name_plural = u"Kategorie slidera"


class BlockSlider(models.Model):

    BOX_SIZES = (
        (12, '12/276'),
        (9, '9/276'),
        (8, '8/276'),
        (7, '7/276'),
        (6, '6/276'),
        (5, '5/276'),
        (4, '4/276'),
        (3, '3/276'),
        (2, '2/276'),
    )
    BG_COLORS = (
        ('#FFFFFF', 'Biały'),
        ('#2d3234', 'Ciemno szary'),
        ('#1f2224', 'Ciemniejszy szary'),
        ('#e74a05', 'Pomarańczowy')
    )

    title = models.CharField(u"Tytuł", max_length=255)
    category = models.ForeignKey(BlockSliderCategory, verbose_name=u'Kategoria', blank=True, null=True)
    content = models.TextField(u"Treść w HTML", blank=True, null=True)
    background = models.ImageField(u"Obrazek tła", upload_to="blockslider", blank=True, null=True)
    background_color = models.CharField(verbose_name=u'Kolor tła', choices=BG_COLORS, default="#FFFFFF", max_length=50)
    url = models.CharField(u"Link", max_length=255, help_text=u"Dla przycisku więcje", null=True, blank=True)
    more_button_text = models.CharField(u'Tekst przycisku więcej', max_length=100, blank=True, null=True, help_text=u'Domyślnie "zobacz"')
    box_size = models.PositiveSmallIntegerField(verbose_name=u'Rozmiar na stronie', choices=BOX_SIZES, default=1, help_text="Ilość kolumn Bootstrap'a / wysokość w px.")
    full_height = models.BooleanField(verbose_name=u'Pełna wysokość', default=False)
    visible = models.BooleanField(u"Widoczny na stronie", default=True)
    without_margins = models.BooleanField(u"Bez marginesów", default=False)
    order = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = u'blockslider'
        verbose_name = u"Slider blokowy"
        verbose_name_plural = u"Slider blokowy"


class BlockSliderFile(models.Model):
    user_file = models.FileField(u"Plik", upload_to="blockslider_files")
    block = models.ForeignKey(BlockSlider)