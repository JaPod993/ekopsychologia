#coding: utf-8
from django.db import models


class NewsletterEmail(models.Model):

    email = models.EmailField(u"Email", unique=True)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletter"

    def __unicode__(self):
        return self.email
