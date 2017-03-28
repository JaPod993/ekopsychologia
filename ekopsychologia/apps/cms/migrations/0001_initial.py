# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import bitfield.models
import datetime
import corecms.fields
import mptt.fields
import picklefield.fields
import corecms.models.base_element
import django.db.models.deletion
from django.conf import settings
import taggit.managers
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('for_lang', models.BooleanField(default=True, verbose_name='Dost\u0119pne w wybranym j\u0119zyku')),
                ('for_lang_pl', models.BooleanField(default=True, verbose_name='Dost\u0119pne w wybranym j\u0119zyku')),
                ('template', models.CharField(max_length=255, null=True, verbose_name='Szablon', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name='Status', choices=[(0, b'Ukryty'), (1, b'Publikowany')])),
                ('identity', models.CharField(default=b'', max_length=255, verbose_name='Tytu\u0142')),
                ('identity_pl', models.CharField(default=b'', max_length=255, null=True, verbose_name='Tytu\u0142')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ostatnia aktualizacja')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('article_date', models.DateTimeField(default=datetime.datetime.now, help_text='Data wy\u015bwietlana przy artykule', verbose_name='Data')),
                ('shortcut', models.TextField(verbose_name='Skr\xf3t')),
                ('slug', models.SlugField(help_text='Unikalny identyfikator kategorii (opcjonalny)', max_length=255, verbose_name='Klucz', blank=True)),
                ('slug_pl', models.SlugField(max_length=255, blank=True, help_text='Unikalny identyfikator kategorii (opcjonalny)', null=True, verbose_name='Klucz')),
                ('content', models.TextField(default=b'', verbose_name='Tre\u015b\u0107', blank=True)),
                ('content_pl', models.TextField(default=b'', null=True, verbose_name='Tre\u015b\u0107', blank=True)),
                ('thumbnail', corecms.fields.Base64ImageField(upload_to=b'', null=True, verbose_name='Miniaturka', blank=True)),
                ('main_image', corecms.fields.Base64ImageField(upload_to=b'', null=True, verbose_name='Obrazek przewodni', blank=True)),
                ('alternative_url', models.CharField(default=b'', help_text=b'Link na kt\xc3\xb3ry bedzie wskazywa\xc5\x82a ten artyku\xc5\x82', max_length=255, verbose_name='Link alternatywny', blank=True)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Autor', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-article_date'],
                'abstract': False,
                'verbose_name': 'Artyku\u0142',
                'verbose_name_plural': 'Artyku\u0142y',
            },
            bases=(corecms.models.base_element.ConnectedFilesMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ConfigCMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_title', models.CharField(default=b'', max_length=255, verbose_name='Tytu\u0142 strony', blank=True)),
                ('site_pagination', models.IntegerField(default=5, verbose_name='Ilo\u015b\u0107 artyku\u0142\xf3w na jednej stronie')),
                ('seo_keywords', models.CharField(default=b'', help_text='Rozdzielaj przecinkiem', max_length=255, verbose_name='S\u0142owa kluczowe', blank=True)),
                ('seo_description', models.TextField(default=b'', verbose_name='Opis w META', blank=True)),
                ('tracking_code', models.TextField(default=b'', verbose_name='Kod \u015bledz\u0105cy w znaczniku HEAD', blank=True)),
                ('cookie_description', models.TextField(default=b'', help_text='Je\u017celi puste to informacja b\u0119dzie niewidoczna', verbose_name='Informacja w informacji o ciastkach', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Konfiguracja',
                'verbose_name_plural': 'Konfiguracja',
            },
        ),
        migrations.CreateModel(
            name='FormGeneratorModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa')),
                ('emails', models.TextField(null=True, verbose_name='E-Maile rozdzielone przecinkami', blank=True)),
                ('form_data', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa')),
            ],
            bases=(corecms.models.base_element.ConnectedFilesMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('for_lang', models.BooleanField(default=True, verbose_name='Dost\u0119pne w wybranym j\u0119zyku')),
                ('for_lang_pl', models.BooleanField(default=True, verbose_name='Dost\u0119pne w wybranym j\u0119zyku')),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('name', models.CharField(default=b'', max_length=255, verbose_name=b'Oryginalna nazwa pliku')),
                ('title', models.CharField(default=b'', max_length=255, verbose_name=b'Tytu\xc5\x82 pliku')),
                ('path', models.FilePathField(max_length=255)),
                ('position', positions.fields.PositionField(default=0)),
                ('distinction', bitfield.models.BitField(((b'downloadable', 'Do pobrania', b'glyphicon-download-alt'), (b'gallery', 'Galeria', b'glyphicon-picture'), (b'cover', 'Poka\u017c ok\u0142adk\u0119', b'glyphicon-book')), default=None)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Data utworzenia')),
                ('file_type', models.CharField(max_length=100, verbose_name=b'Typ pliku', blank=True)),
                ('file_size', models.CharField(max_length=200, verbose_name=b'Rozmiar pliku', blank=True)),
                ('description', models.TextField(max_length=250, verbose_name=b'Opis', blank=True)),
                ('repository', models.BooleanField(default=False, verbose_name='W repozytorium')),
                ('publish', models.BooleanField(default=True, verbose_name='Publikuj na www')),
                ('content_type', models.ForeignKey(related_name='+', blank=True, to='contenttypes.ContentType', null=True)),
                ('created_by', models.ForeignKey(verbose_name=b'Utworzone przez', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(related_name='ghost_files', to='cms.MediaFile', null=True)),
            ],
            options={
                'ordering': ['position'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa')),
                ('slug', models.SlugField(help_text='Unikalny identyfikator', max_length=32, verbose_name='Klucz')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='RelationArticleSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', positions.fields.PositionField(default=-1)),
                ('main', models.BooleanField(default=False)),
                ('child', models.ForeignKey(to='cms.Article')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RelationMenuSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', positions.fields.PositionField(default=-1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template', models.CharField(max_length=255, null=True, verbose_name='Szablon', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name='Status', choices=[(0, b'Ukryty'), (1, b'Publikowany')])),
                ('identity', models.CharField(default=b'', max_length=255, verbose_name='Tytu\u0142')),
                ('identity_pl', models.CharField(default=b'', max_length=255, null=True, verbose_name='Tytu\u0142')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ostatnia aktualizacja')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('alternative_url', models.CharField(default=b'', help_text=b'Link na kt\xc3\xb3ry bedzie wskazywa\xc5\x82a ta strona', max_length=255, verbose_name='Link alternatywny', blank=True)),
                ('thumbnail', corecms.fields.Base64ImageField(upload_to=b'', null=True, verbose_name='Miniaturka', blank=True)),
                ('main_image', corecms.fields.Base64ImageField(upload_to=b'', null=True, verbose_name='Obrazek przewodni', blank=True)),
                ('slug', models.SlugField(help_text='Unikalny identyfikator kategorii (opcjonalny)', max_length=255, verbose_name='Klucz', blank=True)),
                ('slug_pl', models.SlugField(max_length=255, blank=True, help_text='Unikalny identyfikator kategorii (opcjonalny)', null=True, verbose_name='Klucz')),
                ('content', models.TextField(default=b'', verbose_name='Tre\u015b\u0107', blank=True)),
                ('content_pl', models.TextField(default=b'', null=True, verbose_name='Tre\u015b\u0107', blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('articles', models.ManyToManyField(to='cms.Article', through='cms.RelationArticleSite')),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Autor', to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='Strona nadrz\u0119dna', blank=True, to='cms.Site', null=True)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Ostatnio aktualizowa\u0142', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('lft',),
                'abstract': False,
                'verbose_name': 'Strona',
                'verbose_name_plural': 'Strony',
            },
            bases=(corecms.models.base_element.ConnectedFilesMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(verbose_name='Identyfikator')),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Nazwa', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slidery',
            },
        ),
        migrations.CreateModel(
            name='SliderRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, verbose_name='Nazwa', blank=True)),
                ('text', models.TextField(default=b'', verbose_name='Opis', blank=True)),
                ('image', models.ImageField(upload_to=b'public/sliders', verbose_name='Obrazek', blank=True)),
                ('order', models.IntegerField(default=1, verbose_name='Priorytet')),
                ('status', models.IntegerField(default=1, verbose_name='Status', choices=[(0, b'Ukryty'), (1, b'Publikowany')])),
                ('url', models.CharField(default=b'', max_length=255, verbose_name='Url', blank=True)),
                ('parent', models.ForeignKey(related_name='items', to='cms.Slider')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': 'Slider - wpis',
                'verbose_name_plural': 'Slider - wpisy',
            },
        ),
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.SlugField(unique=True, max_length=255, verbose_name='Identyfikator')),
                ('content', models.TextField(default=b'', verbose_name='Tre\u015b\u0107', blank=True)),
                ('content_pl', models.TextField(default=b'', null=True, verbose_name='Tre\u015b\u0107', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Blok tekstowy',
                'verbose_name_plural': 'Bloki tekstowe',
            },
            bases=(corecms.models.base_element.ConnectedFilesMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
            ],
            options={
                'verbose_name': 'Tag',
                'proxy': True,
                'verbose_name_plural': 'Tagi',
            },
            bases=('taggit.tag',),
        ),
        migrations.AddField(
            model_name='relationmenusite',
            name='child',
            field=models.ForeignKey(to='cms.Site'),
        ),
        migrations.AddField(
            model_name='relationmenusite',
            name='parent',
            field=models.ForeignKey(to='cms.Menu'),
        ),
        migrations.AddField(
            model_name='relationarticlesite',
            name='parent',
            field=models.ForeignKey(to='cms.Site'),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tagi'),
        ),
        migrations.AddField(
            model_name='article',
            name='sites',
            field=models.ManyToManyField(to='cms.Site', through='cms.RelationArticleSite'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tagi'),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_by',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Ostatnio aktualizowa\u0142', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.CreateModel(
            name='RepositoryMediaFile',
            fields=[
            ],
            options={
                'verbose_name': 'Plik',
                'proxy': True,
                'verbose_name_plural': 'Repozytorium plik\xf3w',
            },
            bases=('cms.mediafile',),
        ),
        migrations.AlterUniqueTogether(
            name='relationmenusite',
            unique_together=set([('child', 'parent')]),
        ),
        migrations.AlterUniqueTogether(
            name='relationarticlesite',
            unique_together=set([('child', 'parent')]),
        ),
    ]
