from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import rest_framework_swagger as rfs
import json
from django.utils.safestring import mark_safe
from django.shortcuts import render_to_response, RequestContext
from pos.models import Sales, ProductTypes, SalesAgent


def permission_denied_handler(request):
    if not request.user.is_authenticated() or not request.user.is_superuser:
        return HttpResponseRedirect(settings.API_LOGIN_URL)
    template_name = rfs.SWAGGER_SETTINGS.get('template_path')
    data = {
        'swagger_settings': {
            'discovery_url': "%s/api-docs/" % get_full_base_path(request),
            'api_key': rfs.SWAGGER_SETTINGS.get('api_key', ''),
            'token_type': rfs.SWAGGER_SETTINGS.get('token_type'),
            'enabled_methods': mark_safe(
                json.dumps(rfs.SWAGGER_SETTINGS.get('enabled_methods'))),
            'doc_expansion': rfs.SWAGGER_SETTINGS.get('doc_expansion', ''),
        }
    }
    response = render_to_response(
        template_name, RequestContext(request, data))

    return response


def get_full_base_path(request):
    try:
        base_path = rfs.SWAGGER_SETTINGS['base_path']
    except KeyError:
        return request.build_absolute_uri(request.path).rstrip('/')
    else:
        protocol = 'https' if request.is_secure() else 'http'
        return '{0}://{1}'.format(protocol, base_path.rstrip('/'))


class ReportsView(APIView):

    def get(self, request, format=None):
        report = {
            "products": [
            ],
            "agents": [
            ],
            "markers": {}
        }
        organization = request.query_params['organization']
        products = ProductTypes.objects.filter(
            organization=organization).distinct("name")
        agents = SalesAgent.objects.filter(organization=organization)
        for product in products:
            report["products"].append(
                {
                    "name": product.name,
                    "count": Sales.objects.filter(product=product).count()
                }
            )
        for agent in agents:
            report["agents"].append(
                {
                    "name": agent.profile.get_full_name(),
                    "count": Sales.objects.filter(agent=agent).count()
                }
            )
        all_sales = Sales.objects.all()

        for index, sale in enumerate(all_sales):
            if sale.latitude and sale.longitude:
                marker = {
                    ""+"marker"+str(index): {
                        "lat": sale.latitude,
                        "lng": sale.longitude,
                        "message": sale.product.name
                    }
                }
                report["markers"].update(marker)
        return Response(report)
