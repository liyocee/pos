from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^', include('rest_framework_swagger.urls')),
    url(r'^api/', include('api.urls', namespace='api')),
)
