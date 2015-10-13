from rest_framework import generics, permissions
from .models import(
    Organization, SalesAgent, ProductTypes,
    Sales
)
from .serializers import(
    OrganizationSerializer, SalesAgentSerializer,
    ProductTypesSerializer, SalesSerializer)
from .filters import(
    OrganizationFilter, SalesAgentFilter, ProductTypesFilter,
    SalesFilter)


class OrganizationView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_class = OrganizationFilter
    permission_classes = (permissions.AllowAny,)


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class SalesAgentView(generics.ListCreateAPIView):
    queryset = SalesAgent.objects.all()
    serializer_class = SalesAgentSerializer
    filter_class = SalesAgentFilter


class SalesAgentDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = SalesAgent.objects.all()
    serializer_class = SalesAgentSerializer


class ProductTypesView(generics.ListCreateAPIView):
    queryset = ProductTypes.objects.all()
    serializer_class = ProductTypesSerializer
    filter_class = ProductTypesFilter


class ProductTypesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductTypes.objects.all()
    serializer_class = ProductTypesSerializer


class SalesView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filter_class = SalesFilter


class SalesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
