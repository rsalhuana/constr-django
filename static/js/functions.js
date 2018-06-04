var loc = window.location;
var pathName = loc.pathname.substring(loc.pathname.lastIndexOf('/'));
console.log(pathName)
if(pathName == '/'){
	$('.main').addClass('main-width')
}

$(document).ready(function() {
    $('#data_comprobantes').DataTable();
    $('#data_comprobantes_length').hide();
    $('#data_comprobantes_filter').hide();
    $('#data_proyectos').DataTable()
    $('#data_proyectos_length').hide();
    $('#data_proyectos_filter').hide();
    if($('#idEditarIngreso').val()){
    	recorrerDetalle()
    }
    if($('#idVista').val() == 0){
    	$('#opcion_detalle-0').addClass('hide')
    	$('#boton_confor').removeClass('offset-5')
    	$('#boton_confor').addClass('offset-7')
    	$('#form_edit_ingreso').find('input, textarea, button, select').attr('disabled','disabled');
    	$('#tabla_detalle tr').each(function(key) {
    		id= key + 1;
    		$('#opcion_detalle-'+id).addClass('hide')
		});
    }else{
    	 $('#boton_editar').removeClass('hide')
    	$('#boton_editar').addClass('show')

    	if($('#idModal').val() == 1){
     		$('#modal_success').modal('show');  
     	}
     	if($('#idModal').val() == 2){
     		$('#modal_edit').modal('show');  
     	}
    }
     if($('#idVistaProyecto').val() == 0){
     	$('#boton_editar').addClass('hide')
     	$('#boton_regresar').addClass('offset-8')
    	$('#form_editar_proyecto').find('input, textarea, button, select').attr('disabled','disabled');
     }
     if($('#idConformidad').val() == 1){
     	if($('#idConformidadEdit').val() == ""){
     		recorrerConformidad();
     	}
     }
      if($('#idModalConf').val() == 1){
     	$('#modal_success').modal('show');  
     }
} );

function recorrerConformidad(){
	$('#array').val('[]');
	var cont =0;
	var fila = {};
	var lista = JSON.parse($('#array').val());
	var count=11;
	$('#estado').empty();
	$('#tabla_conformidad tr td').each(function(key , value) {
		id1= $(this).attr('id');
		id2 = id1.split('-');
		id = id2[0];
		value = this.id; 
		if( value == 'check1_detalle-'+id2[1]){
			if($("#check_1_"+id2[1]).is(':checked')){
				fila['check1_detalle'] = 1;
			}else{
			fila['check1_detalle'] = 0;
			}	
		}
		if( value == 'check2_detalle-'+id2[1]){
			if($("#check_2_"+id2[1]).is(':checked')){
				fila['check2_detalle'] = 1;
			}else{
			fila['check2_detalle'] = 0;
			}	
		}
		if( value == 'id_detalle-'+id2[1]){
			fila['id_detalle'] = $("#id_detalle-"+id2[1]).text()
		}
		if('check1_detalle-'+id2[1] == value || 'check2_detalle-'+id2[1] == value ){
			if( $("#check_1_"+id2[1]).is(':checked') && $("#check_2_"+id2[1]).is(':checked') ) {  
				x=0
			}
			else{
				cont = 1
			}
		}
		if(count == key){
		lista.push(JSON.stringify(fila))
		count=count+12;
		}
	});
	if(cont == 1){
		$("#estado").append('<option value=11>Rev.Devuelto</option>');
	}else{
		$("#estado").append('<option value=9>Rev.Conforme</option>');
	}
	$('#array').val(JSON.stringify(lista))	
}


function recorrerDetalle(){
	var fila = {};
	var cont = parseInt($('#contador_detalle').val()) + 1;
	var lista = JSON.parse($('#array').val());
	var cont=16
	$('#tabla_detalle tr td').each(function(key , value) {
		id1= $(this).attr('id');
		id2 = id1.split('-');
		id = id2[0];
		value = this.id; 
		if(id == 'direccion_gasto'){
			fila['direccion_gasto'] = $('#direccion_gasto_edit-'+id2[1]).text();
		}else{
			fila[id] = $('#'+id1).text();
		}
		if(cont == key){
			lista.push(JSON.stringify(fila))
			cont=cont+17
		}
	});
	$('#array').val(JSON.stringify(lista))	
}

function selectOrden(){
	if( $("#c_orden").is(':checked')) {  
		$('#num_orden').attr('readonly' , false)
	}else{
		$('#num_orden').attr('readonly' , true)
	}
}

$('#fecha_emision').datepicker({
    format: 'dd/mm/yyyy',
});

function buscarRuc(){
	ruc = $("#ruc").val();
	$.ajax({
		data: {'ruc': ruc},
		url: '/buscarRuc',
		type: 'post',
		success : function(data) {
		 	if(data.length >= 1){
		    	$('#razon_social').val(data[0]['vc_razonsocial']);
		    	$('#id_proveedor').val(data[0]['id_proveedor']);
		    }else{
		    	$('#razon_social').val('');
		    }
		},
	});
}



function recorrerProyectos(type){
	var count=0;
	var count1=0
	if(type==2){$("#buscar").val('');
	$('#no_registro').remove();}
	$('.tr_proyectos').each(function(key , value) {
		 id1= $(this).attr('id');
		 id2 = id1.split('_');
		 id = id2[1];
		 var cont = 0;
		 $(" #tr_"+id+" td" ).each(function(key , value) {
		 	var d = ($(this).eq(0).text()).toLowerCase()
		 	var buscar = ($("#buscar").val()).toLowerCase()
		 	var x = d.search(buscar)
		 	if(x >= 0){
		 		cont = 1
		 	}
		 });
		 if(cont == 1){
		 	$("#tr_"+id).removeClass('hide');
		 	$("#tr_"+id).addClass('show');
		 }
		 else{
		 	$("#tr_"+id).removeClass('show');
		 	$("#tr_"+id).addClass('hide');
		 	count++;
		 }
	count1++;
	});
	if(count == count1){
		$('#no_registro').remove();
		$('#tabla_proyectos').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
	if(count == 0 && count1 ==0 && type == 2){
		$('#no_registro').remove();
		$('#tabla_proyectos').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
}

function exportar(){
	$.ajax({
		url: '/exportar',
		type: 'post',
		success : function(data) {
		},
	});
}

function modalExportar(){
	$('#modal_exportar').modal('show');
}

function modalExportarProyecto(){
	$('#modal_exportar-proyecto').modal('show');
}


function setIngreso(id){
	$("#idIngreso").val(id);
	if($("#estadoIngreso_"+id).val() == 8){
		$('#msg_noti').text('¿Está seguro que desea anular el comprobante ingresado?');
	}else{
		$('#msg_noti').text('¿Está seguro que desea actualizar el estado?');
	}
}

function actualizarComprobante(){
	id = $("#idIngreso").val()
	$.ajax({
		data: {id: id,
			   idEstado:$("#estadoIngreso_"+id).val()},
		url: '/actualizarComprobante',
		type: 'post',
		success : function(data) {
		 	$('#modalInfo').modal('show');
			 $('#tabla_comprobante').html(data);
		},
	});
}

function buscarDocumento(){
	$.ajax({
		data: {'documento': $("#numero_documento").val()},
		url: '/buscarNumDocumento',
		type: 'post',
		success : function(data) {
		 	if(data){
		 		console.log(data[0]['vc_codTipoDocumento'])
		 		tipoDocumento = data[0]['vc_codTipoDocumento']
		 		$('#tipo_documento').val(tipoDocumento);
		    	$('#razon_social').val(data[0]['vc_razonSocial']);
		    	$('#id_cliente').val(data[0]['id_cliente']);
		    }
		},
	});
}

$('.datep').datepicker({
    format: 'dd/mm/yyyy',
});

function setProyecto(id , idEstado){
	$("#idProyecto").val(id);
	$("#idEstadoProyecto").val(idEstado);
	if(idEstado != 16){
		$('#modal-eliminar-proyecto').modal('show');
		$('#body-modal-eliminar').text('¿Está seguro de activar este registro?');
	}else{
		if(idEstado == 16){
			$('#modal-eliminar-proyecto').modal('show');
			$('#body-modal-eliminar').text('¿Está seguro de anular el registro?');
		}else{
			$('#modal_notification').modal('show');
		}
	}
}

function estatusProyecto(){
	$.ajax({
		data: {id: $("#idProyecto").val(),
			   idEstado:$("#idEstadoProyecto").val()},
		url: '/estatusProyecto',
		type: 'post',
		success : function(data) {
		 	$('#modalInfo').modal('show');
			 $('#tabla_proyectos').html(data);
		},
	});
}


$(document).on('click', 'a.link-submit', function (e) {
e.preventDefault();
	var form = $('#' + $(this).data('form'));
	var idform = $(this).attr('data-form');
	var mainclass = $(this).data('formmain') == undefined ? 'nonclass' : '.' + $(this).data('formmain');
	var valid = true;
	var input = "";
	$.each(form.find(mainclass + ' input[required],' + mainclass + ' select[required]'), function (item, index) {
		input ="";
		if ($.trim($(this).val()) == "") {
			valid = false
			input = input + $('label[for="' + $(this).attr('id') + '"]').text() + ' es requerido';
			$('.invalid__'+$(this).attr('id')).html(input)
			$('.invalid__'+$(this).attr('id')).show()
			$('#'+$(this).attr('id')).addClass('invalid')
		 }else{
	 	$('.invalid__'+$(this).attr('id')).hide()
	 	$('#'+$(this).attr('id')).removeClass('invalid')
 		}
 	});
	if (valid) {
		if(idform == "form-save-ingreso" || idform =="form_edit_ingreso"){
			if($('#razon_social').val() != ""){
				form.submit();
			}else{
				$('#modal_agregar').modal('show');
			}
		}
		else if(idform == "form-save-proyecto" || idform =="form_editar_proyecto"){
			if($('#razon_social').val() != ""){
				form.submit();
			}else{
				$('#modal_agregar_proyecto').modal('show');
			}
		}else{
			form.submit();
		}
	} 
});


$(".remove-selected").change(function() {
	 	$('.invalid__'+$(this).attr('id')).hide()
 	$('#'+$(this).attr('id')).removeClass('invalid')
});


function mensajeRevConforme(){
	$('#modal_rev_devuelto').modal('show');
}

function mensajeEdoRegistrado(){
	$('#modal_edo_registrado').modal('show');
}

function mensajeTerminado(){
	$('#modal_terminado').modal('show');
}

function cerrarModal(){
	$('#modal_exportar').modal('hide');
}

function cerrarModalProyecto(){
	$('#modal_exportar-proyecto').modal('hide');
}

function comm_replace(a) {
    ~a.value.indexOf(",") && (a.value = a.value.replace(",", "."));
}

function decimal(pre, de, id) {    	
    $("#" + id).numeric({
        maxPreDecimalPlaces: pre,
        maxDecimalPlaces: de
    });
} 