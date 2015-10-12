from django.conf.urls import patterns, url

from .views import (
    UserListView, UserDetailView, UsersCreateView,
)

urlpatterns = patterns(
    '',
    url(r'^create/$', UsersCreateView.as_view(), name="create"),
    url(r'^$', UserListView.as_view(), name="users"),
    url(r'^(?P<pk>[^/]+)/$', UserDetailView.as_view(), name="user_detail"),
)
