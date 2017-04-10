#coding: utf-8
from django import forms

from website.models import NewsletterEmail


class NewsletterSignForm(forms.Form):

    email = forms.EmailField(label="Email")

    def save(self):
        NewsletterEmail.objects.get_or_create(email=self.cleaned_data["email"])