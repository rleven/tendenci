from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tendenci.core.base.views',
    url(r'^image-preview/(?P<app_label>\w+)/(?P<model>\w+)/(?P<id>\d+)/(?P<size>(\d+|\d+x\d+))/$', 'image_preview', name="image_preview"),
    url(r'^feedback/$', 'feedback', name='tendenci_feedback'),
    url(r'^memcached-status/$', 'memcached_status', name='memcached_status'),
    url(r'^clear-cache/$', 'clear_cache', name='clear_cache'),
    url(r'^password_again/$', 'password_again', name="password_again"),
    url(r'^exception-test/$', 'exception_test', name="exception_test"),
    url(r'^timeout-test/$', 'timeout_test', name="timeout_test"),
)
