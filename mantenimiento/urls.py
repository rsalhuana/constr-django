from django.conf.urls import include, url
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [       
		url(r'^clientes$', views.clientes, name='clientes'),
		url(r'^exportar/clientes$', views.exportarClientes, name='exportar_clientes'),
		url(r'^editar/cliente/(?P<idCliente>\d+)/(?P<idVista>\d+)/$', views.editarCliente, name='editar_cliente'),
		url(r'^editar/cliente$', views.guardarEditarCliente, name='guardar_editar_cliente'),
		url(r'^nuevo/cliente$', views.nuevoCliente ,name="nuevo_cliente"),
		url(r'^guardar/cliente$', views.guardarCliente, name='guardar_cliente'),
		url(r'^activar/cliente/(?P<idCliente>\d+)$', views.activeCliente, name='activar_cliente'),
		url(r'^desactivar/cliente/(?P<idCliente>\d+)$', views.desactiveCliente, name='desactivar_cliente'),

		url(r'^colaboradores$', views.colaboradores, name='colaboradores'),
		url(r'^nuevo/colaborador$', views.nuevoColaborador ,name="nuevo_colaborador"),
		url(r'^guardar/colaborador$', views.guardarColaborador, name='guardar_colaborador'),
		url(r'^exportar/colaborador$', views.exportarColaboradores, name='exportar_colaboradores'),
		url(r'^editar/colaborador$', views.guardarEditarColaborador, name='guardar_editar_colaborador'),
		url(r'^editar/colaborador/(?P<idColaborador>\d+)/(?P<idVista>\d+)/$', views.editarColaborador, name='editar_colaborador'),
		url(r'^activar/colaborador/(?P<idColaborador>\d+)$', views.activeColaborador, name='activar_colaborador'),
		url(r'^desactivar/colaborador/(?P<idColaborador>\d+)$', views.desactiveColaborador, name='desactivar_colaborador'),

		url(r'^proveedores$', views.proveedores, name='proveedores'),
		url(r'^nuevo/proveedor$', views.nuevoProveedor ,name="nuevo_proveedor"),
		url(r'^guardar/proveedor$', views.guardarProveedor, name='guardar_proveedor'),
		url(r'^exportar/proveedor$', views.exportarProveedores, name='exportar_proveedores'),
		url(r'^editar/proveedor$', views.guardarEditarProveedor, name='guardar_editar_proveedor'),
		url(r'^editar/proveedor/(?P<idProveedor>\d+)/(?P<idVista>\d+)/$', views.editarProveedor, name='editar_proveedor'),
		url(r'^activar/proveedor/(?P<idProveedor>\d+)$', views.activeProveedor, name='activar_proveedor'),
		url(r'^desactivar/proveedor/(?P<idProveedor>\d+)$', views.desactiveProveedor, name='desactivar_proveedor'),

		url(r'^proyectos$', views.proyectos, name='proyectos'),
		url(r'^nuevo/proyecto$', views.post_nuevoMantenimiento ,name="nuevo_mant"),
		url(r'^buscarNumDocumento$', views.buscarNumDocumento, name='busca_documento'),
		url(r'^exportar/proyecto$', views.exportarProyectos, name='exportar_proyectos'),
		url(r'^guardar/proyecto$', views.guardarProyecto, name='guardar_proyecto'),
		url(r'^editar/proyecto/(?P<idProyecto>\d+)/(?P<idVista>\d+)/$', views.editarProyecto, name='editar_proyecto'),
		url(r'^editar/proyecto$', views.guardarEditarProyecto, name='guardar_editar_proyecto'),
		url(r'^estatusProyecto$', views.estatusProyecto, name='estatus_proyecto'),

		url(r'^materiales$', permission_required('mantenimiento.view_materiales')(views.materiales), name='materiales'),
		url(r'^nuevo/material$', permission_required('mantenimiento.add_materiales')(views.MaterialesCreateView.as_view()), name='index'),
		url(r'^editar/material/(?P<pk>[0-9]+)/(?P<tipo>\d+)$', permission_required('mantenimiento.change_materiales')(views.MaterialesUpdateView.as_view()), name='editar_material'),
		url(r'^buscarMateriales$', views.buscarMateriales, name='buscar_materiales'),
		url(r'^exportar/materiales/(?P<search>[a-zA-Z0-9]+)/$', views.exportarMateriales, name='exportar_materiales'),
		url(r'^activar/material/(?P<idMaterial>\d+)$', views.activeMaterial, name='activar_material'),
		url(r'^desactivar/material/(?P<idMaterial>\d+)$', views.desactiveMaterial, name='desactivar_material'),
		url(r'^notificar/material$', views.viewNotificar ,name="view_notificar"),
		url(r'^notificar/materiales$', views.notificarMaterial ,name="notificar_material"),
		url(r'^aprobar/material$', views.viewAprobar ,name="view_aprobar"),
		url(r'^aprobar/materiales/(?P<idMaterial>\d+)$', views.aprobarMaterial ,name="aprobar_material"),
		url(r'^verificar/(?P<idMaterial>\d+)$', views.verificar ,name="verificar"),
		url(r'^buscarAprobados$', views.buscarAprobados, name='buscar_aprobados'),
		url(r'^desaprobar/(?P<idMaterial>\d+)$', views.desaprobarMaterial, name='desaprobar_material'),
		url(r'^notificar/aprobado$', views.viewNotificarAprobados ,name="view_notificar_aprobados"),
		url(r'^generarCodigo$', views.generarCodigo ,name="generar_codigo"),
		


]