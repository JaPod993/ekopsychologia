# -*- encoding: utf-8 -*-
import copy

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class AccessListFilter(admin.SimpleListFilter):
    title = 'Uprawnienia'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'access'

    def lookups(self, request, model_admin):
        return (
            ('is_superuser', 'Superuser'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'is_superuser':
            return queryset.filter(is_superuser=True)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "is_active", "is_staff", "is_superuser", )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("password", "email", "first_name", "last_name", "is_active", "is_staff", "is_superuser",)

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = u'<a href="password/">Formularz zmiany hasła</a>'

    def clean_password(self):
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = (AccessListFilter,)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ['first_name', 'last_name', 'email', 'password',]}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser', ]}),
    )
    add_fieldsets = (
        (None, {
            'fields': ['first_name', 'last_name', 'email', 'password1', 'password2']}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser', ]}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = copy.deepcopy(super(MyUserAdmin, self).get_fieldsets(request, obj))
        for row in fieldsets:
            if 'is_superuser' in row[1]['fields'] and not request.user.is_superuser:
                row[1]['fields'].remove('is_superuser')
        return fieldsets

admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
