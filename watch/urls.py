

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views 
from hood import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'',include ('hood.urls')),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',hood_views.activate, name='activate'),
    
    url(r'^login/$', views.login, name = 'login'),
    url(r'^logout/$', views.logout,{ 'next_page': '/'}, name = 'logout')

]
