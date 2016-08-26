from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^time2eat/', include('time2eat.urls', namespace='time2eat')),
    url(r'^admin/', include(admin.site.urls)),
]
