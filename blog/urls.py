from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    url(r'^$', views.login_form),
    url(r'^post_list', views.post_list,name='post_list'),
    url(r'^post_detail/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post_write_form', views.post_write_form, name='post_write_form'),
    url(r'^save_post', views.save_post, name='save_post'),
    url(r'^post_edit_form/(?P<pk>[0-9]+)/$', views.post_edit_form, name='post_edit_form'),
    url(r'^edit_post/(?P<pk>[0-9]+)/$', views.edit_post, name='edit_post'),
    url(r'^delete_post/(?P<pk>[0-9]+)/$', views.delete_post, name='delete_post'),
    url(r'^login_form', views.login_form, name='login_form'),
    url(r'^logout', views.logout, name='logout'),

    url(r'^login_action', views.login_action, name='login_action'),


]
