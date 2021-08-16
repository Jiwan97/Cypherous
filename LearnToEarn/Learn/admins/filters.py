import django_filters
from django_filters import CharFilter


class VFilter(django_filters.FilterSet):
    title_contains = CharFilter(label='Search News :', field_name='heading', lookup_expr='icontains')


class VFilter1(django_filters.FilterSet):
    title_contains = CharFilter(label='Search Course :', field_name='course_name', lookup_expr='icontains')
