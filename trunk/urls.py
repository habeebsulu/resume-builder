from django.conf.urls.defaults import *

urlpatterns = patterns('resume-builder.views',
    (r'^$', 'resume'),
    (r'^pdf/$', 'render_pdf'),
    (r'^pdf/(?P<profile>[a-zA-Z]+)/$', 'render_pdf'),
    (r'^projects/$', 'projects'),
    (r'^projects/(?P<project_slug>[\w\+-]+)/$', 'project_details'),
    )

