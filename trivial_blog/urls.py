from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivial_blog.views.home', name='home'),
    # url(r'^trivial_blog/', include('trivial_blog.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment these two lines to enable your static files on PythonAnywhere
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
