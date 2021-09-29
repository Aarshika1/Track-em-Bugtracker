import django_filters
from django.db.models import fields
from .models import *

class BugFilter(django_filters.FilterSet):
    class Meta:
        model = Bug
        fields = "__all__"
        exclude = ['name','project_id','desc','comments']
