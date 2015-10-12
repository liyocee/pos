from django.conf.urls import patterns, url
from .views import (
    OrganizationView, OrganizationDetailView,
    SalesAgentView, SalesAgentDetailView,
    ProductTypesView, ProductTypesDetailView,
    SalesView, SalesDetailView
)

urlpatterns = patterns(
    '',
    url(r'^product_types/$', ProductTypesView.as_view(),
        name="product_type"),
    url(r'^product_types/(?P<pk>[^/]+)/$',
        ProductTypesDetailView.as_view(),
        name="product_type_details"),

    url(r'^organization/$', OrganizationView.as_view(),
        name="organization"),
    url(r'^organization/(?P<pk>[^/]+)/$',
        OrganizationDetailView.as_view(), name="organization_details"),

    url(r'^sales/$', SalesView.as_view(), name="sales"),
    url(r'^sales/(?P<pk>[^/]+)/$',
        SalesDetailView.as_view(), name="sales_details"),

    url(r'^agent/$', SalesAgentView.as_view(), name="agent"),
    url(r'^agent/(?P<pk>[^/]+)/$', SalesAgentDetailView.as_view(),
        name="agent_details"),
)
