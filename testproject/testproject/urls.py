from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.templatetags.static import static
import testproject
from testproject.settings import BASE_DIR
import website
from website.views import SimplePageView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sbjj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'website.views.index', name='home'),
    #url(r'^about$', 'website.views.about', name='about'),
    url(r'^classes$', 'website.views.classes', name='classes'),
    url(r'^staff$', 'website.views.staff', name="staff"),
    url(r'^staff/(?P<staff_name>\w+)/$', 'website.views.staffdetail', name='staff_detail'),
    url(r'^media$', 'website.views.media', name='media'),
    url(r'^account$','website.views.account', name='account'),
    url(r'^merchandise', 'website.views.merchandise', name='merchandise'),
    url(r'^camps$', 'website.views.camps', name='camps'),
    url(r'^(.+)/', SimplePageView.as_view(), name='simplepage'),
    
)
'''
urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('', (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': BASE_DIR+'/static/'}))

urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': BASE_DIR+'/media/'}))
'''