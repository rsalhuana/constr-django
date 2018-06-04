from django.conf.urls import include, url
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
        url(r'^$', views.post_index),
        url(r'^ingresos/$', views.post_ingresos ,name="ingresos"),
        url(r'^nuevo/$', views.post_nuevo ,name="nuevo"),
        url(r'^buscarRuc$', views.buscarRuc, name='buscarRuc'), 
        url(r'^buscarMaterial$', views.buscarMaterial, name='buscarMaterial'), 
        url(r'^buscarCodMaterial$', views.buscarCodMaterial, name='buscarCodMaterial'), 
        url(r'^buscarDescMaterial$', views.buscarDescMaterial, name='buscarDescMaterial'),
        #url(r'^buscarDescMaterial/(?P<codigo>\D+)/$', views.buscarDescMaterial, name='buscarDescMaterial'),
        url(r'^guardar$', views.guardar, name='guardar'),
	url(r'^exportar/$', views.exportar, name='exportar_ingresos'),
	url(r'^actualizarComprobante$', views.actualizarComprobante, name='actualizarComprobante'),
	url(r'^editar/(?P<idIngreso>\d+)/(?P<idVista>\d+)/$', views.editar, name='editar'),
	url(r'^editarIngreso$', views.editarIngreso, name='editar_ingreso'),
	url(r'^conformidad/(?P<idIngreso>\d+)/$', views.conformidad, name='conformidad'), 
	url(r'^guardarConformidad$', views.guardarConformidad, name='guardar_conformidad'),

]