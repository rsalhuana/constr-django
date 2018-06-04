$('#tabla_materiales, #tabla_poraprobar , #tabla_notificar').DataTable();
$('#tabla_materiales_length , #tabla_poraprobar_length , #tabla_notificar_length').hide();
$('#tabla_materiales_filter , #tabla_poraprobar_filter , #tabla_notificar_filter').hide();
var loc = window.location;
var pathName = loc.pathname.substring(loc.pathname.lastIndexOf('/'));
pathName = pathName.split('/');
console.log(pathName)
$('#id_vc_codigo').attr('readonly','readonly');
if(pathName[1] == "0"){
	$('#btn_save, #id_new_color').hide();
	$('#form-save-materiales').find('input,  select').attr('readonly','readonly');
}
if(pathName[1] == "1"){
	$('#id_new_color').hide();
	$('#id_vc_codigo , #id_id_codTipoGasto').attr('readonly','readonly');
	$('#id_id_codTipoGasto').css('pointer-events','none')
}


var idAprobarTabla = $('#data_poraprobar').closest('tbody').find('tr:eq(0)').text();
if(idAprobarTabla.trim() == 'No se encontraron registros'){
	$('#id_notificar_aprobar').hide();
	$('#id_regresar_aprobar').addClass('offset-6')
}

var idNotificar = $('#data_notificar').closest('tbody').find('tr:eq(0)').text();
if(idNotificar.trim() == 'No se encontraron registros'){
	$('#id_notificar_poraprobar').hide();
	$('#id_regresar_poraprobar').addClass('offset-6')
}

if($('#idNotificarMsg').val() == 3){
	$('#modal_notificar_msg').modal('show');
}

function buscarMateriales(type){
	if(type == 1){
		$("#busqueda").val('');
	}
	$.ajax({
		data: {'id_edit' : $("#permiso_edit").val(),
			'id_delete' : $("#permiso_delete").val(),
			'id_ver' : $("#permiso_ver").val(),
			'busqueda': $("#busqueda").val()},
		url: '/buscarMateriales',
		type: 'post',
		success : function(data) {
		 	$('#tabla_materiales').html('');
            $('#tabla_materiales').html(data);
		},
	});
}

function modalExportMaterial(){
	var descripcion = $('#data_materiales').closest('tbody').find('tr:eq(0)').text();
	var busqueda = $('#busqueda').val();
	if  (busqueda == ""){ busqueda = 0;}
	if(descripcion.trim() == 'Para esta búsqueda no existen Datos'){
		$('#modal_exportar_data').modal('show');
	}else{
		$('#modal_export_material').attr("href" , "exportar/materiales/"+busqueda)
		$('#modal_exportar_materiales').modal('show');
	}
}


function modalStatusMaterial(idMaterial , status){
	if(status == 43){
		$('#activar_material').modal('show');
		$('#id_activar_material').attr("onclick" , "activarMaterial("+idMaterial+","+status+")")
	}else{
		$('#desactivar_material').modal('show');
		$('#id_desactivar_material').attr("onclick" , "desactivarMaterial("+idMaterial+","+status+")")
	}
}

function activarMaterial(idMaterial , status){
	$.ajax({
		url: '/activar/material/'+idMaterial,
		type: 'post',
		success : function(data) {
			$('#modalInfo').modal('show');
			$('#tabla_materiales').html('');
            $('#tabla_materiales').html(data);
		},
	});
}

function desactivarMaterial(idMaterial , status){
	$.ajax({
		url: '/desactivar/material/'+idMaterial,
		type: 'post',
		success : function(data) {
			$('#modalInfo').modal('show');
			$('#tabla_materiales').html('');
            $('#tabla_materiales').html(data);
		},
	});
}

function validarCorreo(email){
    var caract = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (caract.test(email) == false){
        $('#email_valid').text('Debe introducir un correo electronico valido')
        return false;
    }else{
    	$('#email_valid').text('')
        return true;
    }
}

function buscarAprobados(type){
	if(type == 1){
		$("#busqueda").val('');
	}
	$.ajax({
		data: {'busqueda': $("#busqueda").val()},
		url: '/buscarAprobados',
		type: 'post',
		success : function(data) {
		 	$('#tabla_materiales').html('');
            $('#tabla_materiales').html(data);
		},
	});
}

function modalStatusEdicion(){
	$('#status_edicion').modal('show');
}

function selectColor(value){
	if (value == 36){
		$('#id_vc_valor1').attr('readonly',false);
	}else{
		$('#id_vc_valor1').attr('readonly','readonly');
		$('#id_vc_codigo').val('');
	}
}

function generarCodigo(id) {
	$.ajax({
		data: {'id': id},
		url: '/generarCodigo',
		type: 'post',
		success : function(data) {
			$('#span_codigo').text(data);
			$('#href_aprobar').attr("onclick" , "aprobarMaterial("+id+")")
			$('#modal_aprobar_material').modal('show');
		},
	});

}

function aprobarMaterial(id){
	$.ajax({
		data: {'codigo': $('#span_codigo').text()},
		url: '/aprobar/materiales/'+id,
		type: 'post',
		success : function(data) {
			$('#modal_aprobar_material').modal('hide');
			$('#tabla_poraprobar').html('');
	        $('#tabla_poraprobar').html(data);
	        $('#modal_success').modal('show')
	        $('#div_notificar').append('<input type-"hidden" value="'+id+'" name="id_notificar_aprobados">')
		},
	});
}

function modalDesaprobarMaterial(id){
	$('#id_material_desaprobar').val(id);
	$('#modal_desaprobar_material').modal('show');
}

$('#observacion_desaprobar').keyup(function(e){
	if($('#observacion_desaprobar').val() == ""){
		$('#error_id_material_desaprobar').show();
	}else{
		$('#error_id_material_desaprobar').hide();
	}

});

function desaprobarMaterial(){
	var observacion = $('#observacion_desaprobar').val();
	if(observacion){
		$.ajax({
			data: {'observacion': observacion},
			url: '/desaprobar/'+$('#id_material_desaprobar').val(),
			type: 'post',
			success : function(data) {
				$('#modal_desaprobar_material').modal('hide');
			 	$('#tabla_poraprobar').html('');
	            $('#tabla_poraprobar').html(data);
	            $('#modal_success').modal('show')
			},
		});
	}else{
		$('#error_id_material_desaprobar').show();
	}
}

function cerrarModalesMaterial(id){
	$('#'+id).modal('hide');
}