import django_filters
from rest_framework import ISO_8601
from django.utils.encoding import force_str
from django import forms
from django.utils.dateparse import parse_datetime


class IsoDateTimeField(forms.DateTimeField):
    def strptime(self, value, format):
        value = force_str(value)
        if format == ISO_8601:
            parsed = parse_datetime(value)
            if parsed is None:  # Continue with other formats if doesn't match
                raise ValueError
            return parsed
        return super(IsoDateTimeField, self).strptime(value, format)


class IsoDateTimeFilter(django_filters.DateTimeFilter):
    """ Extend ``DateTimeFilter`` to filter by ISO 8601 formated dates too"""
    field_class = IsoDateTimeField


class ListFilterMixin(object):

    def sanitize(self, value_list):
        """
        remove empty items
        """
        return [v for v in value_list if v != u'']

    def customize(self, value):
        return value

    def filter(self, qs, value):
        multiple_vals = value.split(u",")
        multiple_vals = self.sanitize(multiple_vals)
        multiple_vals = map(self.customize, multiple_vals)
        actual_filter = django_filters.fields.Lookup(multiple_vals, 'in')
        return super(ListFilterMixin, self).filter(qs, actual_filter)


class ListCharFilter(ListFilterMixin, django_filters.CharFilter):
    """
    Enable filtering of comma separated strings.
    """
    pass


class ListIntegerFilter(ListCharFilter):
    """
    Enable filtering of comma separated integers.
    """

    def customize(self, value):
        return int(value)


class CommonFieldsFilterset(django_filters.FilterSet):
    """
        Every model that descends from AbstractBase should have this
    """
    updated_before = IsoDateTimeFilter(
        name='updated', lookup_type='lte',
        input_formats=(ISO_8601, '%m/%d/%Y %H:%M:%S'))
    created_before = IsoDateTimeFilter(
        name='created', lookup_type='lte',
        input_formats=(ISO_8601, '%m/%d/%Y %H:%M:%S'))

    updated_after = IsoDateTimeFilter(
        name='updated', lookup_type='gte',
        input_formats=(ISO_8601, '%m/%d/%Y %H:%M:%S'))
    created_after = IsoDateTimeFilter(
        name='created', lookup_type='gte',
        input_formats=(ISO_8601, '%m/%d/%Y %H:%M:%S'))

    updated_on = IsoDateTimeFilter(
        name='updated', lookup_type='exact',
        input_formats=(ISO_8601, '%m/%d/%Y %H:%M:%S'))
    created_on = IsoDateTimeFilter(
        name='created', lookup_type='exact',
        input_formats=(ISO_8601, '%m/%d/%Y %H:%M:%S'))

    is_deleted = django_filters.BooleanFilter(
        name='deleted', lookup_type='exact')
    is_active = django_filters.BooleanFilter(
        name='active', lookup_type='exact')
