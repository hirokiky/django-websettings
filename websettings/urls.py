from django.conf.urls import url, patterns


urlpatterns = patterns('',
    url(r'^$', 'websettings.views.list_view', name='list'),
    url(r'^edit/$', 'websettings.views.edit_view', name='edit'),
)
