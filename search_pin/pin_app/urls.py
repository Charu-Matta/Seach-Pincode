from django.conf.urls import  patterns,url
from pin_app import views
urlpatterns = patterns('' ,
                       url(r'^$', views.first_page),
                        url(r'^search_pincode/$',views.search_pincode, name="search_pincode"), 
                        url(r'^add_entry/$',views.add_entry, name="add_entry"),   #mapping the view with urls
                       
                       )

