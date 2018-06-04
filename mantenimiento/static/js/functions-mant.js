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

function buscarDocumento(){
	$.ajax({
		data: {'documento': $("#numero_documento").val()},
		url: '/buscarNumDocumento',
		type: 'post',
		success : function(data) {
		 	if(data && data[0]){
		 		console.log(data[0]['vc_codTipoDocumento']);
		 		tipoDocumento = data[0]['vc_codTipoDocumento'];
		 		$('#tipo_documento').val(tipoDocumento);
		    	$('#razon_social').val(data[0]['vc_razonSocial']);
		    	$('#id_cliente').val(data[0]['id_cliente']);
		    }
		},
	});
}