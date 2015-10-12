from django.conf.urls import patterns, include, url
from django.contrib import admin

v1_urls = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls', namespace='users')),
    url(r'^auth/', include('rest_auth.urls', namespace='rest_auth')),
    url(r'^auth/registration/', include('rest_auth.registration.urls',
        namespace='rest_auth_registration')),
    url(r'^auth/drf/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(r'^pos/', include('pos.urls', namespace='pos')),
)


urlpatterns = patterns(
    '',
    url(r'^v1/', include(v1_urls, namespace='v1'))
)
