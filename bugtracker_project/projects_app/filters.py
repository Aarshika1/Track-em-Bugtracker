import django_filters
from django.db.models import fields
from .models import *
from django.forms.widgets import Input

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ['organization_name','desc']
      