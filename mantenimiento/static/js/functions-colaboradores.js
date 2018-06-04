function modalExportarColaboradores(){
	$('#modal_exportar-colaboradores').modal('show');
}

function cerrarModalColaboradores(){
	$('#modal_exportar-colaboradores').modal('hide');
}

function recorrerColaboradores(type){
	var count=0;
	var count1=0
	if(type==2){
		$("#buscar").val('');
		$('#no_registro').remove();
	}
	$('.tr_colaboradores').each(function(key , value) {
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
		$('#tabla_colaboradores').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
	if(count == 0 && count1 ==0 && type == 2){
		$('#no_registro').remove();
		$('#tabla_colaboradores').append('<tr id="no_registro"><td colspan="11" class="text-center color-row">No se encontraron registros</td></tr> ')
	}
}

function modalStatusColaborador(idColaborador , status){
	if(status == 2){
		$('#activar_colaborador').modal('show');
		$('#id_activar_colaborador').attr("onclick" , "activarColaborador("+idColaborador+","+status+")")
	}else{
		$('#desactivar_colaborador').modal('show');
		$('#id_desactivar_colaborador').attr("onclick" , "desactivarColaborador("+idColaborador+","+status+")")
	}
}

function activarColaborador(idColaborador , status){
	$.ajax({
		url: '/activar/colaborador/'+idColaborador,
		type: 'post',
		success : function(data) {
			$('#modalInfo').modal('show');
			$('#tabla_colaboradores').html('');
            $('#tabla_colaboradores').html(data);
		},
	});
}

function desactivarColaborador(idColaborador , status){
	$.ajax({
		url: '/desactivar/colaborador/'+idColaborador,
		type: 'post',
		success : function(data) {
			$('#modalInfo').modal('show');
			$('#tabla_colaboradores').html('');
            $('#tabla_colaboradores').html(data);
		},
	});
}