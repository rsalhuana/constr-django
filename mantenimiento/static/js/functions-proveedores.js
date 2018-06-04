function modalExportarProveedores(){
	$('#modal_exportar-proveedores').modal('show');
}

function cerrarModalProveedores(){
	$('#modal_exportar-proveedores').modal('hide');
}

function recorrerProveedores(type){
	var count=0;
	var count1=0
	if(type==2){
		$("#buscar").val('');
		$('#no_registro').remove();
	}
	$('.tr_proveedores').each(function(key , value) {
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
		$('#tabla_proveedores').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
	if(count == 0 && count1 ==0 && type == 2){
		$('#no_registro').remove();
		$('#tabla_proveedores').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
}

function modalStatusProveedor(idProveedor , status){
	if(status == 2){
		$('#activar_proveedor').modal('show');
		$('#id_activar_proveedor').attr("onclick" , "activarProveedor("+idProveedor+","+status+")")
	}else{
		$('#desactivar_proveedor').modal('show');
		$('#id_desactivar_proveedor').attr("onclick" , "desactivarProveedor("+idProveedor+","+status+")")
	}
}

function activarProveedor(idProveedor , status){
	$.ajax({
		url: '/activar/proveedor/'+idProveedor,
		type: 'post',
		success : function(data) {
			$('#modalInfo').modal('show');
			$('#tabla_proveedores').html('');
            $('#tabla_proveedores').html(data);
		},
	});
}

function desactivarProveedor(idProveedor , status){
	$.ajax({
		url: '/desactivar/proveedor/'+idProveedor,
		type: 'post',
		success : function(data) {
			$('#modalInfo').modal('show');
			$('#tabla_proveedores').html('');
            $('#tabla_proveedores').html(data);
		},
	});
}