from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'contacts.views.show_contacts'),
    url(r'^editdata/$', 'contacts.views.edit_data'),
    url(r'^postcontacts/$', 'contacts.views.post_contacts'),
)
