from django.conf.urls import patterns, include, url


urlpatterns = patterns('inflr3.store.views',
    url(r'^$', 'home', name='home'),
    url(r'^products/$', 'productlist', name='productlist'),
    url(r'^products/form/$', 'addproduct', name='addproduct'),
    url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),

    )