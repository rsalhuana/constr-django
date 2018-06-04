from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import login
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_done

urlpatterns = [
    url(r'^a/', admin.site.urls), 	
    url(r'^accounts/login/', login, {'template_name': 'accounts-login.html'}, name='login'),
    url(r'^accounts/logout$', views.LogoutView.as_view(), name='logout'),


    url(r'^$', login_required(views.HomeView.as_view()), name='home'),
    
    url(r'^password_reset/$', views.UserResetPassword.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, {'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'reset/done', password_reset_complete, {'template_name':'password_reset_complete.html'}, name='password_reset_complete'),
#   
#    url(r'^accounts/user/$', permission_required('auth.view_user')(views.UserListView.as_view()), name='accounts-index'),
#    url(r'^accounts/user/add$', permission_required('auth.add_user')(views.UserCreate.as_view()), name='accounts-create'),
]
