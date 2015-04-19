from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'FlashBox.views.home', name='home'),

    # we will match every other url with this line
    url(r'^notes/(?P<url>[a-f0-9]{32})/$', 'FlashBox.views.view_cards', name='view_cards'),
    # url(r'^FlashBox/', include('FlashBox.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
