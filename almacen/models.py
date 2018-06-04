from django.db import models

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    vc_codEstado = models.CharField(db_column='vc_codEstado', max_length=3)  # Field name made lowercase.
    vc_codTipoDocumento = models.ForeignKey('GeneralDetalle', db_column='vc_codTipoDocumento', on_delete=models.PROTECT)  # Field name made lowercase.
    vc_numDocumento = models.CharField(db_column='vc_numDocumento', max_length=12)  # Field name made lowercase.
    vc_razonSocial = models.CharField(db_column='vc_razonSocial', max_length=120)  # Field name made lowercase.
    vc_correo = models.CharField(max_length=80, blank=True, null=True)
    id_ubigeo = models.ForeignKey('Ubigeo', db_column='id_ubigeo', blank=True, null=True, on_delete=models.PROTECT)
    vc_direccion = models.CharField(max_length=150, blank=True, null=True)
    vc_contacto = models.CharField(max_length=120, blank=True, null=True)
    vc_telefono = models.CharField(max_length=12, blank=True, null=True)
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vs_test = models.CharField(db_column='vc_test1', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes'

class Colaborador(models.Model):
    id_colaborador = models.AutoField(primary_key=True)
    vc_codigocolaborador = models.CharField(db_column='vc_codigoColaborador', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vc_codcondicion = models.CharField(db_column='vc_codCondicion', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vc_codtipotrabajador = models.CharField(db_column='vc_codTipoTrabajador', max_length=3, blank=True, null=True)  # Field name made lowercase.
    bl_fldiscapasitado = models.TextField(db_column='bl_flDiscapasitado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    vc_codtipodocumento = models.CharField(db_column='vc_codTipoDocumento', max_length=3)  # Field name made lowercase.
    vc_numdocumento = models.CharField(db_column='vc_numDocumento', max_length=12)  # Field name made lowercase.
    vc_nomColaborador = models.CharField(db_column='vc_nomColaborador', max_length=50)  # Field name made lowercase.
    vc_apePatColaborador = models.CharField(db_column='vc_apePatColaborador', max_length=50)  # Field name made lowercase.
    vc_apematcolaborador = models.CharField(db_column='vc_apeMatColaborador', max_length=50)  # Field name made lowercase.
    id_ubigeo = models.ForeignKey('Ubigeo', db_column='id_ubigeo', blank=True, null=True, on_delete=models.PROTECT)
    vc_direccioncolaborador = models.CharField(db_column='vc_direccionColaborador', max_length=150, blank=True, null=True)  # Field name made lowercase.
    vc_correopersonal = models.CharField(db_column='vc_correoPersonal', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vc_correocorporativo = models.CharField(db_column='vc_correoCorporativo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dt_fecnacimiento = models.DateField(db_column='dt_fecNacimiento', blank=True, null=True)  # Field name made lowercase.
    dt_fecingreso = models.DateField(db_column='dt_fecIngreso', blank=True, null=True)  # Field name made lowercase.
    dt_feccese = models.DateField(db_column='dt_fecCese', blank=True, null=True)  # Field name made lowercase.
    vc_telfcolaborador = models.CharField(db_column='vc_telfColaborador', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vc_codestado = models.CharField(db_column='vc_codEstado', max_length=3)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Colaborador'

class ColaboradoresCargo(models.Model):
    id_colaboradoresCargo = models.AutoField(db_column='id_colaboradoresCargo', primary_key=True)  # Field name made lowercase.
    id_colaborador = models.ForeignKey(Colaborador, db_column='id_colaborador', on_delete=models.PROTECT)
    vc_codCargo = models.ForeignKey('GeneralDetalle', db_column='vc_codCargo', on_delete=models.PROTECT)  # Field name made lowercase.
    b_flagInactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Colaboradores_Cargo'


class General(models.Model):
    id_general = models.AutoField(primary_key=True)
    vc_nomtabla = models.CharField(db_column='vc_nomTabla', max_length=45)  # Field name made lowercase.
    vc_descripcion = models.CharField(max_length=150)
    vc_codestado = models.CharField(db_column='vc_codEstado', max_length=3)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'General'


class GeneralDetalle(models.Model):
    id_generalDetalle = models.AutoField(db_column='id_generalDetalle', primary_key=True)  # Field name made lowercase.
    id_general = models.ForeignKey(General, db_column='id_general', on_delete=models.PROTECT)
    vc_codigo = models.CharField(max_length=3)
    vc_valor1 = models.CharField(max_length=45)
    vc_valor2 = models.CharField(max_length=45, blank=True, null=True)
    vc_valor3 = models.CharField(max_length=45, blank=True, null=True)
    vc_valor4 = models.CharField(max_length=45, blank=True, null=True)
    txt_valor5 = models.TextField(null=True)
    vc_codestado = models.CharField(db_column='vc_codEstado', max_length=3)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'General_Detalle'


class IngresoCabecera(models.Model):
    id_ingresoCabecera = models.AutoField(db_column='id_ingresoCabecera', primary_key=True)  # Field name made lowercase.
    vc_ocRayro = models.CharField(db_column='vc_ocRayro', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vc_codRepcion = models.ForeignKey('GeneralDetalle', db_column='vc_codRepcion', related_name='vc_codRepcion', on_delete=models.PROTECT)  # Field name made lowercase.
    id_proyecto = models.ForeignKey('Proyectos', db_column='id_proyecto', related_name='proyectos', on_delete=models.PROTECT)
    vc_codEstado = models.ForeignKey('GeneralDetalle', db_column='vc_codEstado', related_name='vc_codEstado', on_delete=models.PROTECT)  # Field name made lowercase.
    dt_emision = models.DateField()
    id_proveedor = models.ForeignKey('Proveedor', db_column='id_proveedor', on_delete=models.PROTECT)
    vc_codTipoComprobante = models.ForeignKey('GeneralDetalle', db_column='vc_codTipoComprobante' , related_name='vc_codTopoComprobante', on_delete=models.PROTECT)  # Field name made lowercase.
    vc_serieComprobante = models.CharField(db_column='vc_serieComprobante', max_length=3)  # Field name made lowercase.
    vc_numComprobante = models.CharField(db_column='vc_numComprobante', max_length=5)  # Field name made lowercase.
    vc_codCondicionPago = models.ForeignKey('GeneralDetalle', db_column='vc_codCondicionPago',related_name='vc_codCondicionPago', on_delete=models.PROTECT)  # Field name made lowercase.
    fl_importe = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    fl_igv = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    fl_total = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    b_flagInactivo = models.BooleanField(db_column='b_flagInactivo')  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuarioCrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipCrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioEdita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipEdita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingreso_Cabecera'


class IngresoConformidad(models.Model):
    id_ingresoConformidad = models.AutoField(db_column='id_ingresoConformidad', primary_key=True)  # Field name made lowercase.
    id_ingresoCabecera = models.ForeignKey(IngresoCabecera, db_column='id_ingresoCabecera', on_delete=models.PROTECT)  # Field name made lowercase.
    fl_importeConformidad = models.DecimalField(db_column='fl_importeConformidad', max_digits=9, decimal_places=2) # Field name made lowercase.
    tx_observacionConformidad = models.TextField(db_column='tx_observacionConformidad', blank=True, null=True)  # Field name made lowercase.
    dt_fecConformidad = models.DateTimeField(db_column='dt_fecConformidad')  # Field name made lowercase.
    vc_codConformidad = models.ForeignKey(GeneralDetalle, db_column='vc_codConformidad', on_delete=models.PROTECT)  # Field name made lowercase.
    b_flagInactivo = models.BooleanField(db_column='b_flagInactivo')  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuarioCrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipCrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioEdita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipeEita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingreso_Conformidad'


class IngresoDetalle(models.Model):
    id_ingresoDetalle = models.AutoField(db_column='id_ingresoDetalle', primary_key=True)  # Field name made lowercase.
    id_ingresoCabecera = models.ForeignKey(IngresoCabecera, db_column='id_ingresoCabecera', on_delete=models.PROTECT)  # Field name made lowercase.
    vc_codDireccionGasto = models.ForeignKey(GeneralDetalle, db_column='vc_codDireccionGasto', on_delete=models.PROTECT)  # Field name made lowercase.
    id_materiales = models.ForeignKey('Materiales', db_column='id_materiales', on_delete=models.PROTECT)
    nu_cantidad = models.DecimalField(max_digits=9, decimal_places=2)
    nu_totalIngreso = models.DecimalField(db_column='nu_totalIngreso', max_digits=9, decimal_places=2)  # Field name made lowercase.
    nu_precioUnitario = models.DecimalField(db_column='nu_precioUnitario', max_digits=9, decimal_places=2)  # Field name made lowercase.
    nu_Importe = models.DecimalField(db_column='nu_Importe', max_digits=9, decimal_places=2)  # Field name made lowercase.
    nu_igv = models.DecimalField(max_digits=9, decimal_places=2)
    nu_subTotal = models.DecimalField(db_column='nu_subTotal', max_digits=9, decimal_places=2)
    bl_conformidadOC = models.BooleanField(db_column='bl_conformidadOC')  # Field name made lowercase. This field type is a guess.
    bl_conformidadAdm = models.BooleanField(db_column='bl_conformidadAdm')  # Field name made lowercase. This field type is a guess.
    b_flagInactivo = models.BooleanField(db_column='b_flagInactivo')  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuarioCrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipCrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioEdita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipEdita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingreso_Detalle'


class Materiales(models.Model):
    id_materiales = models.AutoField(primary_key=True)
    vc_codigo = models.CharField(max_length=10, blank=True, null=True)
    id_codEstado = models.ForeignKey('GeneralDetalle', db_column='id_codEstado', related_name='id_codEstado', on_delete=models.PROTECT)  # Field name made lowercase.
    id_codTipoGasto = models.ForeignKey('GeneralDetalle', db_column='id_codTipoGasto', related_name='id_codTipoGasto', on_delete=models.PROTECT)  # Field name made lowercase.
    id_codFamilia = models.ForeignKey('GeneralDetalle', db_column='id_codFamilia', related_name='id_codFamilia', on_delete=models.PROTECT)  # Field name made lowercase.
    id_codClasificacion = models.ForeignKey('GeneralDetalle', db_column='id_codClasificacion', blank=True, null=True , related_name='id_codClasificacion', on_delete=models.PROTECT)  # Field name made lowercase.
    vc_descripcion = models.CharField(max_length=200)
    id_codColor = models.ForeignKey('GeneralDetalle', db_column='id_codColor', blank=True, null=True,  related_name='id_codColor', on_delete=models.PROTECT)  # Field name made lowercase.
    id_unidadMedida = models.ForeignKey('UnidadMedida', db_column='id_unidadMedida', on_delete=models.PROTECT)  # Field name made lowercase.
    nu_valor = models.FloatField()
    nu_stockMinimo = models.FloatField(db_column='nu_stockMinimo', blank=True, null=True)  # Field name made lowercase.
    nu_stockMaximo = models.FloatField(db_column='nu_stockMaximo', blank=True, null=True)  # Field name made lowercase.
    b_flagInactivo = models.BooleanField(db_column='b_flagInactivo')  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuarioCrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipCrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioEdita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipEdita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_codSituacion = models.ForeignKey('GeneralDetalle', db_column='id_codSituacion', related_name='GeneralDetalle', on_delete=models.PROTECT)  # Field name made lowercase.
    nu_stockActual = models.FloatField(db_column='nu_stockActual')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Materiales'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    vc_codestado = models.CharField(db_column='vc_codEstado', max_length=3)  # Field name made lowercase.
    vc_rucproveedor = models.CharField(db_column='vc_rucProveedor', max_length=11)  # Field name made lowercase.
    vc_razonsocial = models.CharField(db_column='vc_razonSocial', max_length=150)  # Field name made lowercase.
    id_ubigeo = models.ForeignKey('Ubigeo', db_column='id_ubigeo', blank=True, null=True, on_delete=models.PROTECT)
    vc_direccion = models.CharField(max_length=150, blank=True, null=True)
    vc_contacto = models.CharField(max_length=100, blank=True, null=True)
    vc_telfcontacto = models.CharField(db_column='vc_telfContacto', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vc_telfempresa = models.CharField(db_column='vc_telfEmpresa', max_length=10, blank=True, null=True)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proveedor'


class Proyectos(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    vc_codEstado =models.ForeignKey('GeneralDetalle', db_column='vc_codEstado', related_name='vc_codEstado_pro', on_delete=models.PROTECT) 
    vc_nombreProyecto = models.CharField(db_column='vc_nombreProyecto', max_length=120)  # Field name made lowercase.
    id_ubigeo = models.ForeignKey('Ubigeo', db_column='id_ubigeo', blank=True, null=True, on_delete=models.PROTECT)
    vc_direccion = models.CharField(max_length=200, blank=True, null=True)
    dt_fecAprobacion = models.DateField(db_column='dt_fecAprobacion', blank=True, null=True)  # Field name made lowercase.
    dt_fecInicio = models.DateField(db_column='dt_fecInicio', blank=True, null=True)  # Field name made lowercase.
    dt_fecCierre = models.DateField(db_column='dt_fecCierre', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.ForeignKey(Colaborador, db_column='id_colaborador', blank=True, null=True, on_delete=models.PROTECT)
    vc_nomContacto = models.CharField(db_column='vc_nomContacto', max_length=120, blank=True, null=True)  # Field name made lowercase.
    vc_telfContacto = models.CharField(db_column='vc_telfContacto', max_length=10, blank=True, null=True)  # Field name made lowercase.
    b_flagInactivo = models.BooleanField(db_column='b_flagInactivo')  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Clientes, db_column='id_cliente', on_delete=models.PROTECT)
    class Meta:
        managed = False
        db_table = 'Proyectos'

class Ubigeo(models.Model):
    id_ubigeo = models.AutoField(primary_key=True)
    vc_codigoubigeo = models.CharField(db_column='vc_codigoUbigeo', max_length=6)  # Field name made lowercase.
    vc_descripcion = models.CharField(max_length=50)
    nu_totalprov = models.DecimalField(db_column='nu_totalProv', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    nu_totaldist = models.DecimalField(db_column='nu_totalDist', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vc_descregion = models.CharField(db_column='vc_descRegion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_codestado = models.CharField(db_column='vc_codEstado', max_length=3)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ubigeo'


class UnidadMedida(models.Model):
    id_unidadMedida = models.AutoField(db_column='id_unidadMedida', primary_key=True)  # Field name made lowercase.
    vc_descripcionlarga = models.CharField(db_column='vc_descripcionLarga', max_length=80)  # Field name made lowercase.
    vc_descripcionCorta = models.CharField(db_column='vc_descripcionCorta', max_length=5)  # Field name made lowercase.
    vc_codtipounidadmedida = models.CharField(db_column='vc_codTipoUnidadMedida', max_length=3)  # Field name made lowercase.
    nu_valor = models.FloatField()
    nu_orden = models.DecimalField(max_digits=2, decimal_places=0)
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Unidad_Medida'
