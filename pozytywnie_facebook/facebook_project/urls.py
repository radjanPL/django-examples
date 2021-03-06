from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'blog.views.home_view', name='home'),
    url(r'^post/(?P<pk>[0-9]+)/$', 'blog.views.post_view', name='post'),
    url(r'^canvas/$', 'canvas_example.views.canvas', name='canvas'),
    url(r'^facebook_javascript_authentication/', include('facebook_javascript_authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
