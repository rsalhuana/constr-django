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

$('#descripcion_detalle').keyup(function(e){
	if($('#direccion_gasto').val() == ""){
		$('#modal_material_desc').modal('show');
	}
	else{
		descripcion = $("#descripcion_detalle").val();
		$.ajax({
			data: {'descripcion': descripcion , 'idTipo': $('#direccion_gasto').val()},
			url: '/buscarMaterial',
			type: 'post',
			success : function(data) {
				var array = [];
			 	$.each(data, function( index, value ) {
	  				array.push(value['vc_descripcion']);
				});
				$(".autocomplete").autocomplete({
	    			source: array,minLength: 1,
	                select: function(event, data) {
	                    $("#descripcion_detalle").val(data['item']['label']);
	                    buscarCodMaterial(data['item']['label']);
	                },
	  		});
				$('.ui-helper-hidden-accessible').hide();
			},
		});
	}
});

function buscarCodMaterial(material) {
	$.ajax({
		data: {'material': material},
		url: '/buscarCodMaterial',
		type: 'post',
		success : function(data) {
			$('#codigo_material').val(data[0]['vc_codigo']);
			$('.invalid__codigo_material').hide()
			$('.invalid__descripcion_detalle').hide()
	 		$('#descripcion_detalle').removeClass('invalid')
	 		$('#codigo_material').removeClass('invalid')
			$('#id_materiales').val(data[0]['id_materiales']);
			$('#valor_medida').val(data[1]);
			$('#unidad_medida').val(data[2]);
			if($('#cantidad_detalle').val() > 0){
				$('#total_detalle').val($('#valor_medida').val()*$('#cantidad_detalle').val())
			}
		},
	});
}


$('#cantidad_detalle').keydown(function(e){
	if(event.which == 188){
		return false;
	}else{
		if($('#cantidad_detalle').val() > 0  || $('#cantidad_detalle').val() == ""){
			if($('#cantidad_detalle').val() == ""){
				$('#total_detalle').val('');
				$('#precio_detalle').val('');
			}
			else{
			calculoCantidad()
			}
		}else{
			$('#modal_valid_data').modal('show');	
		}
	}
});

$('#importe_detalle').keydown(function(e){
	if(event.which == 188){
		return false;
	}else{
		if($('#importe_detalle').val() > 0  || $('#importe_detalle').val() == ""){
			if($('#importe_detalle').val() == ""){
				$('#subtotal_detalle').val('');
				$('#igv_detalle').val('');
			}else{
				calculoImporte()
			}
		}else{
			$('#modal_valid_data').modal('show');
		}
	}
});

function calculoCantidad(){
	if($('#valor_medida').val() > 0){
		$('#total_detalle').val($('#valor_medida').val()*$('#cantidad_detalle').val())
		if($('#importe_detalle').val() > 0 &&  $('#cantidad_detalle').val() > 0){
			var precio = $('#subtotal_detalle').val() / $('#total_detalle').val();
			var total = $('#cantidad_detalle').val() * $('#valor_medida').val();
			$('#precio_detalle').val(precio.toFixed(4));
			$('#total_detalle').val(total.toFixed(2));
		}
	}
}

function calculoImporte(){
	var importe = $('#importe_detalle').val();
	var subtotal = (importe*100)/118;
	var igv = importe - subtotal 
	var precio = subtotal.toFixed(2) / $('#total_detalle').val();
	$('#subtotal_detalle').val(subtotal.toFixed(2));
	$('#igv_detalle').val(igv.toFixed(2));
	if($('#total_detalle').val() != ''){
		$('#precio_detalle').val(precio.toFixed(4));
	}
}

function agregarDetalle() {
	calculoCantidad()
	calculoImporte()
	if($('#cantidad_detalle').val() == 0){
		$('#cantidad_detalle').val('');
		$('#total_detalle').val('');
		$('#precio_detalle').val('');
	}
	if($('#importe_detalle').val() == 0){
		$('#importe_detalle').val('');
		$('#subtotal_detalle').val('');
		$('#igv_detalle').val('');
		$('#precio_detalle').val('');
	}
	var valid = true;
	$('#detalle input , #detalle select').each(function(index , value) {
		var input ="";
		if ($.trim($(this).val()) == "" && $(this).attr('id') != "codigo_material") {
			valid = false
			input = input + $('label[for="' + $(this).attr('id') + '"]').text() + ' es requerido';
			if(input != " es requerido"){
				$('.invalid__'+$(this).attr('id')).html(input)
				$('.invalid__'+$(this).attr('id')).show()
				$('#'+$(this).attr('id')).addClass('invalid')
			}	
		 }else{
	 	$('.invalid__'+$(this).attr('id')).hide()
	 	$('#'+$(this).attr('id')).removeClass('invalid')
 		}
	});
			if($('#id_materiales').val() == ""){
			$('#modal_material').modal('show');
		}
	if (valid) {
		var fila = {};
		var cont = parseInt($('#contador_detalle').val()) + 1;
		$('#contador_detalle').val(cont);
		$("#tabla_detalle").append("<tr id='"+cont+"'>");                         
	    $("#"+cont).append("<td id='direccion_gasto-"+cont+"'>"+$('#direccion_gasto').find(":selected").text()+"</td>");
	    $("#"+cont).append("<td id='codigo_material-"+cont+"'>"+$('#codigo_material').val()+"</td>");
	    $("#"+cont).append("<td id='descripcion_detalle-"+cont+"'>"+$('#descripcion_detalle').val()+"</td>");
	    $("#"+cont).append("<td id='unidad_medida-"+cont+"'>"+$('#unidad_medida').val()+"</td>");
	    $("#"+cont).append("<td id='check1_detalle-"+cont+"'> <input class='text-center' type='checkbox' id='inlineCheckbox1' value='option1' disabled></td>");
	    $("#"+cont).append("<td id='cantidad_detalle-"+cont+"'>"+$('#cantidad_detalle').val()+"</td>");
	    $("#"+cont).append("<td id='total_detalle-"+cont+"'>"+$('#total_detalle').val()+"</td>");
	    $("#"+cont).append("<td id='precio_detalle-"+cont+"'>"+$('#precio_detalle').val()+"</td>");
	    $("#"+cont).append("<td id='igv_detalle-"+cont+"'>"+$('#igv_detalle').val()+"</td>");
	    $("#"+cont).append("<td id='importe_detalle-"+cont+"'>"+$('#importe_detalle').val()+"</td>");
	    $("#"+cont).append("<td id='check2_detalle-"+cont+"'> <input class='text-center' type='checkbox' id='inlineCheckbox1' value='option1' disabled></td>");
	    $("#"+cont).append("<td id='opcion_detalle-"+cont+"'><div class='row margin-button'><div class='cursor' onclick='editarDetalle("+cont+")'><i class='fa fa-pencil-square-o'></i></div><div class='cursor margin-button' onclick='eliminarDetalle("+cont+")'><i class='fa fa-times'></i></div></div></td>");
		$("#"+cont).append("<td id='subtotal_detalle-"+cont+"' class='hide'>"+$('#subtotal_detalle').val()+"</td>");
	    $("#"+cont).append("<td id='valor_medida-"+cont+"' class='hide'>"+$('#valor_medida').val()+"</td>");
	    $("#"+cont).append("<td id='id_detalle-"+cont+"' class='hide'>0</td>");
	    $("#"+cont).append("<td id='direccion_gasto_edit-"+cont+"' class='hide'>"+$('#direccion_gasto').val()+"</td>");
	    $("#"+cont).append("<td id='id_materiales-"+cont+"' class='hide'>"+$('#id_materiales').val()+"</td>");
		$("#tabla_detalle").append("</tr>");

		if($('#idEditarIngreso').val()){
			$('#array').val('[]');
	    	recorrerDetalle()
	    }else{
			var lista = JSON.parse($('#array').val());
			$('#detalle input').each(function(index , value) {
				id = $(this).attr('id');
				id = id.split('-');
				id = id[0];
				value = this.id; 
				fila[value] = this.value;
			});
			fila['direccion_gasto'] = $('#direccion_gasto').val();
			lista.push(JSON.stringify(fila))
			$('#array').val(JSON.stringify(lista))	
		}
		limpiarFormDetalle(cont);
		calculoTotal();
	}
}

function eliminarDetalle(id , edit){
	$('#'+id).remove();
	if($('#idEditarIngreso').val()){
		var fila = [];
		var lista = JSON.parse($('#idActDetalle').val());
		fila = edit;
		lista.push(JSON.stringify(fila))
		$('#idActDetalle').val(JSON.stringify(lista))	
		$('#array').val('[]');
    	recorrerDetalle()
    }
}

function editarDetalle(id){
	$('#botonAgregar').hide();
	$('#botonGuardar').show();
	$('#idEditar').val(id);
	$(" #"+id+" td").each(function (key , value){
		if(key == 0){
  			$("#direccion_gasto").find('option:contains("'+$(this).eq(0).text()+'")').prop('selected', true);
		}else{
			id = $(this).attr('id');
			id = id.split('-');
			id = id[0];
			$('#'+id).val($(this).eq(0).text());
		}
	});
}

function guardarEdicion(){
	calculoCantidad()
	calculoImporte()
	if($('#cantidad_detalle').val() == 0){
		$('#cantidad_detalle').val('');
		$('#total_detalle').val('');
		$('#precio_detalle').val('');
	}
	if($('#importe_detalle').val() == 0){
		$('#importe_detalle').val('');
		$('#subtotal_detalle').val('');
		$('#igv_detalle').val('');
		$('#precio_detalle').val('');
	}
	var valid = true;
	$('#detalle input , #detalle select').each(function(index , value) {
		var input =""
		if ($.trim($(this).val()) == "" && $(this).attr('id') != "codigo_material") {
			valid = false
			input = input + $('label[for="' + $(this).attr('id') + '"]').text() + ' es requerido';
			if(input != " es requerido"){
				$('.invalid__'+$(this).attr('id')).html(input)
				$('.invalid__'+$(this).attr('id')).show()
				$('#'+$(this).attr('id')).addClass('invalid')
			}	
		 }else{
	 	$('.invalid__'+$(this).attr('id')).hide()
	 	$('#'+$(this).attr('id')).removeClass('invalid')
 		}
	});
	if (valid) {
		$('#botonAgregar').show();
		$('#botonGuardar').hide();
		var idEditar = $('#idEditar').val();
		$(" #"+idEditar+" td").each(function (key , value){
			id = $(this).attr('id');
			id = id.split('-');
			id= id[0];
			if(id == "direccion_gasto"){
				$(this).eq(0).text($('#direccion_gasto').find(":selected").text());
			}else{
				$(this).eq(0).text($('#'+id).val());
			}
		});
		limpiarFormDetalle(idEditar);
		if($('#idEditarIngreso').val()){
			$('#array').val('[]');
	    	recorrerDetalle()
	    }
	    calculoTotal();
	}
}

function limpiarFormDetalle(cont){
	$(" #"+cont+" td").each(function (key , value){
		id = $(this).attr('id');
		id = id.split('-');
		id = id[0];
		$('#'+id).val('');
	});
}

function buscarDescMaterial() {
	$.ajax({
		data: {'codigo': $('#codigo_material').val()},
		url: '/buscarDescMaterial',
		type: 'post',
		success : function(data) {
			if(data){
				$('#descripcion_detalle').val(data[0]['vc_descripcion']);
				$('.invalid__descripcion_detalle').hide()
	 			$('#descripcion_detalle').removeClass('invalid')
				$('#id_materiales').val(data[0]['id_materiales']);
				$('#valor_medida').val(data[1]);
				$('#unidad_medida').val(data[2]);
				var codigo = data[0]['vc_codEstado'];
				$('#direccion_gasto').val(codigo);
				if($('#cantidad_detalle').val() > 0){
					$('#total_detalle').val($('#valor_medida').val()*$('#cantidad_detalle').val())
				}
				if($('#precio_detalle').val() == "" && $('#cantidad_detalle').val() != ""){
					$('#precio_detalle').val($('#subtotal_detalle').val() / $('#total_detalle').val());
				}
			}else{
				$('#descripcion_detalle').val('');
				$('#valor_medida').val('');
				$('#unidad_medida').val('');
			}
		},
	});
}

function calculoTotal(){
	var importe = 0;
	var igv = 0;
	$('#tabla_detalle td').each(function(index , value) {
		id = $(this).attr('id');
		id = id.split('-');
		id = id[0];
		if(id == 'subtotal_detalle' ){
			importe = parseFloat(importe) + parseFloat($(this).eq(0).text())
		}
		if(id == 'igv_detalle' ){
			igv = parseFloat(igv) + parseFloat($(this).eq(0).text())
		}
	});
	$('#importe_comprobante').val(importe.toFixed(2));
	$("#igv_comprobante").val(igv.toFixed(2));
	calTotal =  importe + igv;
	$("#total_comprobante").val(calTotal.toFixed(2));
}

function buscar(type){
	
	if(type==2){$("#buscar").val('');}
	recorrerIngresos(type)
}

function recorrerIngresos(type){
	var count=0;
	var count1=0
	if(type==2){$("#buscar").val('');
	$('#no_registro').remove();}
	$('.tr_ingresos').each(function(key , value) {
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
	if(count == count1 && type != 2){
		$('#no_registro').remove();
		$('#tabla_comprobante').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
	if(count == 0 && count1 ==0 && type == 2){
		$('#no_registro').remove();
		$('#tabla_comprobante').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
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

function cerrarModalClientes(){
	$('#modal_exportar-clientes').modal('hide');
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