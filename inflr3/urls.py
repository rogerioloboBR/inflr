from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^conta/', include('inflr3.accounts.urls', namespace='accounts')),
    url(r'^', include('inflr3.store.urls', namespace='store')),

)
