from django.http import HttpResponse
from django.shortcuts import render ,HttpResponse , render_to_response , redirect
from almacen.models import Proyectos , Proveedor , GeneralDetalle , Materiales , UnidadMedida , IngresoCabecera , IngresoDetalle , IngresoConformidad , Ubigeo ,Colaborador , Clientes , ColaboradoresCargo
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime 
import ast
from django.db.models import Q
from django.template.loader import render_to_string
#from django.urls import reverse_lazy
from django.core.urlresolvers import reverse_lazy
from decimal import Decimal

modal = 0
 # Funcion que carga la pagina principal del proyecto 
 # @author cvargas
 # @date 26/03/2018
def post_index(request):
	return render(request, 'almacen.html', {})

 # Funcion que carga todos los comprobantes de ingresos en estado activo 
 # @author cvargas
 # @date 26/03/2018
def post_ingresos(request):
	ingresoCabecera = IngresoCabecera.objects.all().select_related('id_proyecto', 'vc_codEstado', 'id_proveedor', 'vc_codTipoComprobante', 'vc_codCondicionPago')
	return render(request, 'ingresos/ingresos.html', {'ingresoCabecera' : ingresoCabecera})

 # Funcion que carga los  combos y vista para agregar un comprobante
 # @author cvargas
 # @date 26/03/2018
def post_nuevo(request):
	fecha = datetime.now()
	fecha = fecha.strftime("%d/%m/%Y")
	proyectos = Proyectos.objects.all()
	recepcion = GeneralDetalle.objects.filter(id_general= 5 )
	comprobante = GeneralDetalle.objects.filter(id_general= 2 )
	condicion = GeneralDetalle.objects.filter(id_general= 3 )
	gasto = GeneralDetalle.objects.filter(id_general= 6 )
	return render(request, 'ingresos/nuevo.html', {'proyectos': proyectos , 'recepcion':recepcion , 'tipocomprobante' :comprobante 
		,'condicionpago' : condicion , 'direcciongasto' : gasto , 'fecha':fecha})

 # Funcion que permite buscar el numero de razon social del proveedor al que le pertenece el ruc
 # @param  ruc proveedor
 # @author cvargas
 # @date 27/03/2018
@csrf_exempt
def buscarRuc(request):
	ruc = request.POST['ruc']
	proveedor = Proveedor.objects.filter(vc_rucproveedor= ruc ).values('vc_razonsocial', 'id_proveedor')
	return HttpResponse( json.dumps( list(proveedor)), content_type="application/json")

 # Funcion que permite buscar los materiales de acuerdo al parametro enviado en el filtro de busqueda en la vista detalle
 # @param  descripcion material 
 # @author cvargas
 # @date 27/03/2018
@csrf_exempt
def buscarMaterial(request):
	descripcion = request.POST['descripcion']
	idTipo = request.POST['idTipo']
	# material = Materiales.objects.filter(vc_descripcion__icontains= descripcion , id_codEstado = idTipo ).values('vc_descripcion','id_materiales', 'vc_codigo')
	material = Materiales.objects.filter(id_codTipoGasto = idTipo ).values('vc_descripcion','id_materiales', 'vc_codigo')
	return HttpResponse( json.dumps( list(material)), content_type="application/json")

 # Funcion que permite buscar los detalles de acuerdo al codigo de un material
 # @param  codigo material 
 # @author cvargas
 # @date 27/03/2018
@csrf_exempt
def buscarCodMaterial(request):
	descripcion = request.POST['material']
	material = Materiales.objects.filter(vc_descripcion= descripcion ).values('id_unidadMedida', 'vc_codigo' , 'id_materiales')
	list_result = [value for value in material]
	medidas = UnidadMedida.objects.filter(id_unidadMedida=list_result[0]['id_unidadMedida']).get()
	list_result.append(medidas.nu_valor)
	list_result.append(medidas.vc_descripcionCorta)
	return HttpResponse( json.dumps(list(list_result)), content_type="application/json")

 # Funcion que permite buscar los valores de medida correspondientes al material
 # @param  descripcion material 
 # @author cvargas
 # @date 27/03/2018
@csrf_exempt
def buscarDescMaterial(request):
	if request.POST['codigo']:
		material = Materiales.objects.filter(vc_codigo= request.POST['codigo'] ).values('id_unidadMedida', 'vc_descripcion' , 'id_materiales', 'id_codEstado')
	else:
		material = Materiales.objects.filter(Q (vc_codigo= request.POST['codigo']) | Q (vc_codigo= None) ).values('id_unidadMedida', 'vc_descripcion' , 'id_materiales', 'id_codEstado')
	list_result = [value for value in material]
	if list_result:
		medidas = UnidadMedida.objects.filter(id_unidadMedida=list_result[0]['id_unidadMedida']).get()
		list_result.append(medidas.nu_valor)
		list_result.append(medidas.vc_descripcionCorta)
		return HttpResponse( json.dumps(list(list_result)), content_type="application/json")
	else:
		return HttpResponse( json.dumps(False), content_type="application/json")

# Funcion para guardar el ingreso cabecera de un comprobante con cada uno de sus detalles
# @param  ingreso cabecera e ingreso detalle
# @author cvargas
# @date 28/03/2018
def guardar(request):
	x  = request.POST
	date =  datetime.strptime(x.getlist('fecha_emision')[0],'%d/%m/%Y').strftime('%Y-%m-%d') 
	proyecto = Proyectos.objects.get(id_proyecto=x.getlist('proyecto')[0])
	recepcion = GeneralDetalle.objects.get(id_generalDetalle=x.getlist('recepcion')[0])
	estado = GeneralDetalle.objects.get(id_generalDetalle=x.getlist('estado')[0])
	tipoComprobante = GeneralDetalle.objects.get(id_generalDetalle=x.getlist('tipo_comprobante')[0])
	condPago = GeneralDetalle.objects.get(id_generalDetalle=x.getlist('condicion')[0])
	proveedor = Proveedor.objects.get(id_proveedor=x.getlist('id_proveedor')[0])
	
	cabecera = IngresoCabecera(vc_ocRayro=x.getlist('num_orden')[0], vc_codRepcion=recepcion, id_proyecto=proyecto,
		vc_codEstado=estado, dt_emision=date, id_proveedor=proveedor,vc_codTipoComprobante=tipoComprobante, 
		vc_serieComprobante=x.getlist('serie')[0], vc_numComprobante=x.getlist('num_comprobante')[0],
		vc_codCondicionPago=condPago,fl_importe=x.getlist('importe_comprobante')[0],fl_igv=x.getlist('igv_comprobante')[0], 
		fl_total=x.getlist('total_comprobante')[0] , dt_crea = datetime.now() )
	cabecera.save()
	array = x.getlist('array')
	for a in array:
		b = json.loads(a)
		for c in b:
			cdict = ast.literal_eval(c)
			material =  Materiales.objects.get(id_materiales =cdict.get('id_materiales'))
			direccionGasto = GeneralDetalle.objects.get(id_generalDetalle=cdict.get('direccion_gasto'))
			detalle = IngresoDetalle(id_ingresoCabecera=cabecera , vc_codDireccionGasto=direccionGasto,
				id_materiales=material,nu_cantidad=cdict.get('cantidad_detalle'),nu_totalIngreso=cdict.get('total_detalle'),
				nu_precioUnitario=cdict.get('precio_detalle'),nu_Importe=cdict.get('importe_detalle'),
				nu_igv=cdict.get('igv_detalle'),nu_subTotal= cdict.get('subtotal_detalle'), dt_crea = datetime.now(), b_flagInactivo=0,
				bl_conformidadAdm=0,bl_conformidadOC=0)
			detalle.save()
	global modal
	modal =1
	return redirect(reverse_lazy('editar', kwargs={'idIngreso': cabecera.id_ingresoCabecera , 'idVista' : 1}))

# Funcion para exportar en formato excel los comprobantes activos de almacen
# @author cvargas
# @date 28/03/2018
@csrf_exempt
def exportar(request):
	ingresoCabecera =  IngresoCabecera.objects.all().select_related('id_proyecto' , 'id_proveedor')
	template_name = "ingresos/exportar.html"
	response = render_to_response(template_name, {'ingresoCabecera': ingresoCabecera})
	filename = "ingresos.xls"
	response['Content-Disposition'] = 'attachment; filename='+filename
	response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-16'
	return response

# Funcion para actualizar el estado del comprobante seleccionado a Registrado o Anulado
# @param  id del comprobante a actualizar
# @param  id del estado en el que se encuentra el comprobante
# @author cvargas
# @date 28/03/2018
@csrf_exempt
def actualizarComprobante(request):
	idEstado =request.POST['idEstado']
	codigo = 10
	if idEstado != '8':
		codigo = 8
	ingreso = IngresoCabecera.objects.filter(id_ingresoCabecera=request.POST['id']).update(vc_codEstado=codigo)
	ingresoCabecera = IngresoCabecera.objects.all().select_related('id_proyecto' , 'id_proveedor')
	html = render_to_string('ingresos/tabla_ingresos.html', {'ingresoCabecera' : ingresoCabecera})
	return HttpResponse(html)

# Funcion que consulta el detalle del comprobante a editar
# @param  id del comprobante a consultar
# @param  id de la vista de la opcion seleccionada, para conocer si se selecciono la opcion de consulta o de edicion 
# @author cvargas
# @date 29/03/2018
def editar(request , idIngreso , idVista):
	idModal = 0
	global modal 
	if modal == 1:
		idModal = modal
		modal = 0
	if modal ==2:
		idModal = modal
		modal = 0
	ingresoCabecera = IngresoCabecera.objects.filter(id_ingresoCabecera=idIngreso).select_related('id_proveedor').get()
	proyectos = Proyectos.objects.all()
	recepcion = GeneralDetalle.objects.filter(id_general= 5 )
	comprobante = GeneralDetalle.objects.filter(id_general= 2 )
	condicion = GeneralDetalle.objects.filter(id_general= 3 )
	gasto = GeneralDetalle.objects.filter(id_general= 6 )
	estado = GeneralDetalle.objects.filter(id_general= 4 )
	detalles = IngresoDetalle.objects.filter(id_ingresoCabecera= idIngreso , b_flagInactivo=0 ).select_related('vc_codDireccionGasto' , 'id_materiales')
	return render(request, 'ingresos/editar.html', {'ingresoCabecera': ingresoCabecera ,'proyectos': proyectos , 'recepcion':recepcion , 'tipocomprobante' :comprobante 
		,'condicionpago' : condicion , 'direcciongasto' : gasto , 'estado':estado , 'detalles':detalles , 'idVista': idVista, 'idModal':idModal})


# Funcion que guarda la edicion del ingreso cabecera con sus detalles
# @param  id del comprobante a editar
# @param  detalles del comprobante
# @author cvargas
# @date 29/03/2018
def editarIngreso(request):
	data  = request.POST
	date =  datetime.strptime(data.getlist('fecha_emision')[0],'%d/%m/%Y').strftime('%Y-%m-%d') 
	proyecto = Proyectos.objects.get(id_proyecto=data.getlist('proyecto')[0])
	recepcion = GeneralDetalle.objects.get(id_generalDetalle=data.getlist('recepcion')[0])
	estado = GeneralDetalle.objects.get(id_generalDetalle=data.getlist('estado')[0])
	tipoComprobante = GeneralDetalle.objects.get(id_generalDetalle=data.getlist('tipo_comprobante')[0])
	condPago = GeneralDetalle.objects.get(id_generalDetalle=data.getlist('condicion')[0])
	proveedor = Proveedor.objects.get(id_proveedor=data.getlist('id_proveedor')[0])
	cabecera =IngresoCabecera.objects.filter(id_ingresoCabecera=request.POST['idEditarIngreso']).update(vc_ocRayro=data.getlist('num_orden')[0], vc_codRepcion=recepcion, id_proyecto=proyecto,
		vc_codEstado=estado, dt_emision=date, id_proveedor=proveedor,vc_codTipoComprobante=tipoComprobante, 
		vc_serieComprobante=data.getlist('serie')[0], vc_numComprobante=data.getlist('num_comprobante')[0],
		vc_codCondicionPago=condPago,fl_importe=data.getlist('importe_comprobante')[0],fl_igv=data.getlist('igv_comprobante')[0], 
		fl_total=data.getlist('total_comprobante')[0])
	array = data.getlist('array')
	for a in array:
		b = json.loads(a)
		for c in b:
			cdict = ast.literal_eval(c)
			idIngresoDetalle = IngresoDetalle.objects.filter(id_ingresoDetalle=cdict.get('id_detalle'))
			material =  Materiales.objects.get(id_materiales =cdict.get('id_materiales'))
			if idIngresoDetalle:
				actDetalle = IngresoDetalle.objects.filter(id_ingresoDetalle=cdict.get('id_detalle')).update(vc_codDireccionGasto=cdict.get('direccion_gasto'),
				id_materiales=material,nu_cantidad=cdict.get('cantidad_detalle'),nu_totalIngreso=cdict.get('total_detalle'),
				nu_precioUnitario=cdict.get('precio_detalle'),nu_Importe=cdict.get('importe_detalle'),
				nu_igv=cdict.get('igv_detalle'),nu_subTotal= cdict.get('subtotal_detalle'))
			else:
				direccionGasto = GeneralDetalle.objects.get(id_generalDetalle=cdict.get('direccion_gasto'))
				ingreso = IngresoCabecera.objects.get(id_ingresoCabecera=request.POST['idEditarIngreso'])
				detalle = IngresoDetalle(id_ingresoCabecera=ingreso , vc_codDireccionGasto=direccionGasto,
				id_materiales=material,nu_cantidad=cdict.get('cantidad_detalle'),nu_totalIngreso=cdict.get('total_detalle'),
				nu_precioUnitario=cdict.get('precio_detalle'),nu_Importe=cdict.get('importe_detalle'),
				nu_igv=cdict.get('igv_detalle'),nu_subTotal= cdict.get('subtotal_detalle'), dt_crea = datetime.now(),bl_conformidadAdm=0,bl_conformidadOC=0, b_flagInactivo=0)
				detalle.save()

	detalles = request.POST['idActDetalle']
	for det in data.getlist('idActDetalle'):
		values = json.loads(det)
		for val in values:
			cdict = ast.literal_eval(val)
			IngresoDetalle.objects.filter(id_ingresoDetalle=cdict).update(b_flagInactivo = 1, dt_edita = datetime.now())

	detalleActivo = IngresoDetalle.objects.filter(id_ingresoCabecera = request.POST['idEditarIngreso'] , b_flagInactivo = 0)
	if not detalleActivo:
		IngresoCabecera.objects.filter(id_ingresoCabecera=request.POST['idEditarIngreso']).update(fl_total =0 , fl_igv = 0, fl_importe=0)
	global modal
	modal =2
	return redirect(reverse_lazy('editar', kwargs={'idIngreso': request.POST['idEditarIngreso'] , 'idVista' : 1}))

# Funcion para mostrar los detalles del comprobante al que se le dara conformidad
# @param  id del comprobante a editar
# @author cvargas
# @date 29/03/2018
def conformidad(request , idIngreso):
	idModal = 0
	global modal 
	if modal == 1:
		idModal = modal
		modal = 0
	detalles = IngresoDetalle.objects.filter(id_ingresoCabecera= idIngreso , b_flagInactivo=0 ).select_related('vc_codDireccionGasto' , 'id_materiales')
	estado = GeneralDetalle.objects.filter(Q(id_generalDetalle=9) | Q(id_generalDetalle=11) )
	conformidad = IngresoConformidad.objects.filter(id_ingresoCabecera = idIngreso) 
	if not conformidad:
		idConformidad  = False
		importeConformidad =  False
		obConformidad = False
		estadoConformidad = False
	else: 
		for conf in conformidad:
			idConformidad  = conf.id_ingresoConformidad
			importeConformidad =  conf.fl_importeConformidad
			obConformidad = conf.tx_observacionConformidad
			estadoConformidad = conf.vc_codConformidad
	print(obConformidad)
	return render(request, 'ingresos/conformidad.html', {'detalles' : detalles , 'estado':estado , 'idIngreso':idIngreso , 'idConformidad' : idConformidad,
		'importeConformidad':importeConformidad , 'obConformidad':obConformidad, 'estadoConformidad':estadoConformidad, 'idModal':idModal})

# Funcion que guarda la conformidad del comprobante segun el estado especificado
# @param  parametros de la conformidad
# @author cvargas
# @date 29/03/2018
def guardarConformidad(request):
	data  = request.POST
	ingreso = IngresoCabecera.objects.get(id_ingresoCabecera=request.POST['idIngreso'])
	codConformidad = GeneralDetalle.objects.get(id_generalDetalle=request.POST['estado'])
	# total_compra = string.replace(request.POST['total_compra'], ",", ".")
	total_compra = request.POST['total_compra'].replace(",", ".")
	if request.POST['idConformidadEdit']:
		conformidad = IngresoConformidad.objects.filter(id_ingresoConformidad=request.POST['idConformidadEdit']).update(fl_importeConformidad=total_compra ,
		 tx_observacionConformidad=request.POST['observaciones'],vc_codConformidad =codConformidad ,b_flagInactivo=0, dt_edita = datetime.now())
		array = data.getlist('array')
		for a in array:
			b = json.loads(a)
			for c in b:
				cdict = ast.literal_eval(c)
				actDetalle = IngresoDetalle.objects.filter(id_ingresoDetalle=cdict.get('id_detalle')).update(bl_conformidadOC=cdict.get('check1_detalle'),
					bl_conformidadAdm=cdict.get('check2_detalle'))
	else:
		conformidad = IngresoConformidad(id_ingresoCabecera=ingreso,fl_importeConformidad=total_compra ,
		 tx_observacionConformidad=request.POST['observaciones'],dt_fecConformidad = datetime.now(),
		 vc_codConformidad =codConformidad ,b_flagInactivo=0, dt_crea = datetime.now())
		conformidad.save()
		array = data.getlist('array')
		for a in array:
			b = json.loads(a)
			for c in b:
				cdict = ast.literal_eval(c)
				actDetalle = IngresoDetalle.objects.filter(id_ingresoDetalle=cdict.get('id_detalle')).update(bl_conformidadOC=cdict.get('check1_detalle'),
					bl_conformidadAdm=cdict.get('check2_detalle'))
	global modal
	modal =1
	return redirect(reverse_lazy('conformidad', kwargs={'idIngreso': request.POST['idIngreso']}))
