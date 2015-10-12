from common.filters import (
    CommonFieldsFilterset,
    ListCharFilter,
)
from .models import(
    Organization, SalesAgent, ProductTypes,
    Sales
)


class SalesFilter(CommonFieldsFilterset):
    product = ListCharFilter(
        name='product__id', lookup_type='exact'
    )
    customer_email = ListCharFilter(lookup_type='icontains')
    customer_id_number = ListCharFilter(lookup_type='icontains')
    customer_first_name = ListCharFilter(lookup_type='icontains')
    customer_last_name = ListCharFilter(lookup_type='icontains')
    customer_phone = ListCharFilter(lookup_type='icontains')
    customer_email = ListCharFilter(lookup_type='icontains')
    customer_address = ListCharFilter(lookup_type='icontains')

    class Meta(object):
        model = Sales


class OrganizationFilter(CommonFieldsFilterset):
    user_id = ListCharFilter(
        name='profile__id', lookup_type='exact'
    )
    name = ListCharFilter(
        name='profile__firstname', lookup_type='icontains')

    class Meta:
        model = Organization


class SalesAgentFilter(CommonFieldsFilterset):
    user_id = ListCharFilter(
        name='profile__id', lookup_type='exact'
    )
    name = ListCharFilter(
        name='profile__firstname', lookup_type='icontains')
    organization = ListCharFilter(
        name='organization__id', lookup_type='exact')

    class Meta:
        model = SalesAgent


class ProductTypesFilter(CommonFieldsFilterset):
    organization = ListCharFilter(
        name='organization__id', lookup_type='exact')
    name = ListCharFilter(lookup_type='contains')

    class Meta:
        model = ProductTypes
