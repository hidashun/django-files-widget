try:
    from django.conf.urls.defaults import patterns, url
except:
    from django.conf.urls import patterns, url

from django.conf import settings

urlpatterns = patterns("topnotchdev.files_widget.views",
    url('^upload/$', "upload", name="files_widget_upload"),
    url('^thumbnail-url/$', "thumbnail_url", name="files_widget_get_thumbnail_url"),
)
