from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/(?P<auth_error>\d+)/$', 'loginsys.views.auth_login'),
    url(r'^login/$', 'loginsys.views.auth_login'),
    url(r'^logout/$', 'loginsys.views.auth_logout'),

)
