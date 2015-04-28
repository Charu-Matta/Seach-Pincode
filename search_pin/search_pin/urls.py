from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^pin_app/', include('pin_app.urls')), #mapping the application with application url.
  
)
