from rest_framework.filters import django_filters

from .models import Vote


class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        return super(ListFilter, self).filter(
            qs, django_filters.fields.Lookup(value.split(','), 'in')
        )


class VoteFilterSet(django_filters.FilterSet):
    model = django_filters.CharFilter(name='content_type__model')
    ids = ListFilter(name='object_id')

    class Meta:
        model = Vote
