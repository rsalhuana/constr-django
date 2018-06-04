function modalExportarClientes(){
	$('#modal_exportar-clientes').modal('show');
}

function cerrarModalClientes(){
	$('#modal_exportar-clientes').modal('hide');
}

function recorrerClientes(type){
	var count=0;
	var count1=0
	if(type==2){
		$("#buscar").val('');
		$('#no_registro').remove();
	}
	$('.tr_clientes').each(function(key , value) {
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
		$('#tabla_clientes').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
	if(count == 0 && count1 ==0 && type == 2){
		$('#no_registro').remove();
		$('#tabla_clientes').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
}

function modalStatusCliente(idCliente , status){
	if(status == 2){
		$('#activar_cliente').modal('show');
		$('#id_activar_cliente').attr("onclick" , "activarCliente("+idCliente+","+status+")")
	}else{
		$('#desactivar_cliente').modal('show');
		$('#id_desactivar_cliente').attr("onclick" , "desactivarCliente("+idCliente+","+status+")")
	}
}

function activarCliente(idCliente , status){
	$.ajax({
		url: '/activar/cliente/'+idCliente,
		type: 'post',
		success : function(data) {
			$('#modalInfo').modal('show');
			$('#tabla_clientes').html('');
            $('#tabla_clientes').html(data);
		},
	});
}

function desactivarCliente(idCliente , status){
	$.ajax({
		url: '/desactivar/cliente/'+idCliente,
		type: 'post',
		success : function(data) {
			$('#modalInfo').modal('show');
			$('#tabla_clientes').html('');
            $('#tabla_clientes').html(data);
		},
	});
}