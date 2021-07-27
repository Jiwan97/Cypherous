import django_filters
from django_filters import CharFilter


class VFilter(django_filters.FilterSet):
    title_contains = CharFilter(label='Search News :', field_name='heading', lookup_expr='icontains')
