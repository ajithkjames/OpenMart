from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from account.forms import LoginForm
from rest_framework import routers

schema_view = get_swagger_view(title='Employee Management API')

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('market.urls', namespace='market')),
    url(r'^api/', include('account.urls', namespace='account')),
    url(r'^$', views.login, {'template_name': 'login.html', 
	'authentication_form': LoginForm,
	'redirect_authenticated_user': True},name='login'),
    url(r'^logout', views.logout, {'next_page': 'login'},name='logout'),
    url(r'^docs/', schema_view),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)