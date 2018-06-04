# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    vc_codestado = models.CharField(db_column='vc_codEstado', max_length=3)  # Field name made lowercase.
    vc_codtipodocumento = models.ForeignKey('GeneralDetalle', db_column='vc_codTipoDocumento', on_delete=models.PROTECT)  # Field name made lowercase.
    vc_numdocumento = models.CharField(db_column='vc_numDocumento', max_length=12)  # Field name made lowercase.
    vc_razonsocial = models.CharField(db_column='vc_razonSocial', max_length=120)  # Field name made lowercase.
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

    class Meta:
        managed = True
        db_table = 'Clientes'


class Colaborador(models.Model):
    id_colaborador = models.AutoField(primary_key=True)
    vc_codigocolaborador = models.CharField(db_column='vc_codigoColaborador', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vc_codcondicion = models.CharField(db_column='vc_codCondicion', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vc_codtipotrabajador = models.CharField(db_column='vc_codTipoTrabajador', max_length=3, blank=True, null=True)  # Field name made lowercase.
    bl_fldiscapasitado = models.TextField(db_column='bl_flDiscapasitado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    vc_codtipodocumento = models.CharField(db_column='vc_codTipoDocumento', max_length=3)  # Field name made lowercase.
    vc_numdocumento = models.CharField(db_column='vc_numDocumento', max_length=12)  # Field name made lowercase.
    vc_nomcolaborador = models.CharField(db_column='vc_nomColaborador', max_length=50)  # Field name made lowercase.
    vc_apepatcolaborador = models.CharField(db_column='vc_apePatColaborador', max_length=50)  # Field name made lowercase.
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
        managed = True
        db_table = 'Colaborador'


class ColaboradoresCargo(models.Model):
    id_colaboradorescargo = models.AutoField(db_column='id_colaboradoresCargo', primary_key=True)  # Field name made lowercase.
    id_colaborador = models.ForeignKey(Colaborador, db_column='id_colaborador', on_delete=models.PROTECT)
    vc_codcargo = models.ForeignKey('GeneralDetalle', db_column='vc_codCargo', on_delete=models.PROTECT)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
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
        managed = True
        db_table = 'General'


class GeneralDetalle(models.Model):
    id_generaldetalle = models.AutoField(db_column='id_generalDetalle', primary_key=True)  # Field name made lowercase.
    id_general = models.ForeignKey(General, db_column='id_general', on_delete=models.PROTECT)
    vc_codigo = models.CharField(max_length=3)
    vc_valor1 = models.CharField(max_length=45)
    vc_valor2 = models.CharField(max_length=60, blank=True, null=True)
    vc_valor3 = models.CharField(max_length=45, blank=True, null=True)
    vc_valor4 = models.CharField(max_length=45, blank=True, null=True)
    txt_valor5 = models.TextField(blank=True, null=True)
    vc_codestado = models.CharField(db_column='vc_codEstado', max_length=3)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'General_Detalle'


class IngresoCabecera(models.Model):
    id_ingresocabecera = models.AutoField(db_column='id_ingresoCabecera', primary_key=True)  # Field name made lowercase.
    vc_ocrayro = models.CharField(db_column='vc_ocRayro', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vc_codrepcion = models.ForeignKey(GeneralDetalle, db_column='vc_codRepcion', on_delete=models.PROTECT)  # Field name made lowercase.
    id_proyecto = models.ForeignKey('Proyectos', db_column='id_proyecto', on_delete=models.PROTECT)
    vc_codestado = models.ForeignKey(GeneralDetalle, db_column='vc_codEstado', on_delete=models.PROTECT)  # Field name made lowercase.
    dt_emision = models.DateField()
    id_proveedor = models.ForeignKey('Proveedor', db_column='id_proveedor', on_delete=models.PROTECT)
    vc_codtipocomprobante = models.ForeignKey(GeneralDetalle, db_column='vc_codTipoComprobante', on_delete=models.PROTECT)  # Field name made lowercase.
    vc_seriecomprobante = models.CharField(db_column='vc_serieComprobante', max_length=3)  # Field name made lowercase.
    vc_numcomprobante = models.CharField(db_column='vc_numComprobante', max_length=5)  # Field name made lowercase.
    vc_codcondicionpago = models.ForeignKey(GeneralDetalle, db_column='vc_codCondicionPago', on_delete=models.PROTECT)  # Field name made lowercase.
    fl_importe = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    fl_igv = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    fl_total = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Ingreso_Cabecera'


class IngresoConformidad(models.Model):
    id_ingresoconformidad = models.AutoField(db_column='id_ingresoConformidad', primary_key=True, on_delete=models.PROTECT)  # Field name made lowercase.
    id_ingresocabecera = models.ForeignKey(IngresoCabecera, db_column='id_ingresoCabecera', on_delete=models.PROTECT)  # Field name made lowercase.
    fl_importeconformidad = models.DecimalField(db_column='fl_importeConformidad', max_digits=9, decimal_places=2)  # Field name made lowercase.
    tx_observacionconformidad = models.TextField(db_column='tx_observacionConformidad', blank=True, null=True)  # Field name made lowercase.
    dt_fecconformidad = models.DateTimeField(db_column='dt_fecConformidad')  # Field name made lowercase.
    vc_codconformidad = models.ForeignKey(GeneralDetalle, db_column='vc_codConformidad', on_delete=models.PROTECT)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Ingreso_Conformidad'


class IngresoDetalle(models.Model):
    id_ingresodetalle = models.AutoField(db_column='id_ingresoDetalle', primary_key=True)  # Field name made lowercase.
    id_ingresocabecera = models.ForeignKey(IngresoCabecera, db_column='id_ingresoCabecera', on_delete=models.PROTECT)  # Field name made lowercase.
    vc_coddirecciongasto = models.ForeignKey(GeneralDetalle, db_column='vc_codDireccionGasto', on_delete=models.PROTECT)  # Field name made lowercase.
    id_materiales = models.ForeignKey('Materiales', db_column='id_materiales', on_delete=models.PROTECT)
    nu_cantidad = models.DecimalField(max_digits=9, decimal_places=2)
    nu_totalingreso = models.DecimalField(db_column='nu_totalIngreso', max_digits=9, decimal_places=2)  # Field name made lowercase.
    nu_preciounitario = models.DecimalField(db_column='nu_precioUnitario', max_digits=9, decimal_places=2)  # Field name made lowercase.
    nu_importe = models.DecimalField(db_column='nu_Importe', max_digits=9, decimal_places=2)  # Field name made lowercase.
    nu_igv = models.DecimalField(max_digits=9, decimal_places=2)
    nu_subtotal = models.DecimalField(db_column='nu_subTotal', max_digits=9, decimal_places=2)  # Field name made lowercase.
    bl_conformidadoc = models.TextField(db_column='bl_conformidadOC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bl_conformidadadm = models.TextField(db_column='bl_conformidadAdm')  # Field name made lowercase. This field type is a guess.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Ingreso_Detalle'


class Materiales(models.Model):
    id_materiales = models.AutoField(primary_key=True)
    vc_codigo = models.CharField(max_length=10, blank=True, null=True)
    id_codestado = models.ForeignKey(GeneralDetalle, db_column='id_codEstado', on_delete=models.PROTECT)  # Field name made lowercase.
    id_codtipogasto = models.ForeignKey(GeneralDetalle, db_column='id_codTipoGasto', on_delete=models.PROTECT)  # Field name made lowercase.
    id_codfamilia = models.ForeignKey(GeneralDetalle, db_column='id_codFamilia', on_delete=models.PROTECT)  # Field name made lowercase.
    id_codclasificacion = models.ForeignKey(GeneralDetalle, db_column='id_codClasificacion', blank=True, null=True, on_delete=models.PROTECT)  # Field name made lowercase.
    vc_descripcion = models.CharField(max_length=200)
    id_codcolor = models.ForeignKey(GeneralDetalle, db_column='id_codColor', blank=True, null=True, on_delete=models.PROTECT)  # Field name made lowercase.
    id_unidadmedida = models.ForeignKey('UnidadMedida', db_column='id_unidadMedida', on_delete=models.PROTECT)  # Field name made lowercase.
    nu_valor = models.DecimalField(max_digits=9, decimal_places=2)
    nu_stockminimo = models.DecimalField(db_column='nu_stockMinimo', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nu_stockmaximo = models.DecimalField(db_column='nu_stockMaximo', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_codsituacion = models.ForeignKey(GeneralDetalle, db_column='id_codSituacion', on_delete=models.PROTECT)  # Field name made lowercase.
    nu_stockactual = models.DecimalField(db_column='nu_stockActual', max_digits=9, decimal_places=2)  # Field name made lowercase.
    vc_numnotificacion = models.CharField(db_column='vc_numNotificacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vc_observaciondesaprobar = models.CharField(db_column='vc_observacionDesaprobar', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id_statusaprobado = models.IntegerField(db_column='id_statusAprobado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
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
        managed = True
        db_table = 'Proveedor'


class Proyectos(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    vc_nombreproyecto = models.CharField(db_column='vc_nombreProyecto', max_length=120)  # Field name made lowercase.
    id_ubigeo = models.ForeignKey('Ubigeo', db_column='id_ubigeo', blank=True, null=True, on_delete=models.PROTECT)
    vc_direccion = models.CharField(max_length=200, blank=True, null=True)
    dt_fecaprobacion = models.DateField(db_column='dt_fecAprobacion', blank=True, null=True)  # Field name made lowercase.
    dt_fecinicio = models.DateField(db_column='dt_fecInicio', blank=True, null=True)  # Field name made lowercase.
    dt_feccierre = models.DateField(db_column='dt_fecCierre', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.ForeignKey(Colaborador, db_column='id_colaborador', blank=True, null=True, on_delete=models.PROTECT)
    vc_nomcontacto = models.CharField(db_column='vc_nomContacto', max_length=120, blank=True, null=True)  # Field name made lowercase.
    vc_telfcontacto = models.CharField(db_column='vc_telfContacto', max_length=10, blank=True, null=True)  # Field name made lowercase.
    b_flaginactivo = models.TextField(db_column='b_flagInactivo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_crea = models.DateTimeField()
    vc_usuariocrea = models.CharField(db_column='vc_usuarioCrea', max_length=50)  # Field name made lowercase.
    vc_ipcrea = models.CharField(db_column='vc_ipCrea', max_length=20)  # Field name made lowercase.
    dt_edita = models.DateTimeField(blank=True, null=True)
    vc_usuarioedita = models.CharField(db_column='vc_usuarioEdita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_ipedita = models.CharField(db_column='vc_ipEdita', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vc_codestado = models.ForeignKey(GeneralDetalle, db_column='vc_codEstado', blank=True, null=True, on_delete=models.PROTECT)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Clientes, db_column='id_cliente', on_delete=models.PROTECT)

    class Meta:
        managed = True
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
        managed = True
        db_table = 'Ubigeo'


class UnidadMedida(models.Model):
    id_unidadmedida = models.AutoField(db_column='id_unidadMedida', primary_key=True)  # Field name made lowercase.
    vc_descripcionlarga = models.CharField(db_column='vc_descripcionLarga', max_length=80)  # Field name made lowercase.
    vc_descripcioncorta = models.CharField(db_column='vc_descripcionCorta', max_length=5)  # Field name made lowercase.
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
        managed = True
        db_table = 'Unidad_Medida'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete=models.PROTECT)
    permission = models.ForeignKey('AuthPermission', on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.PROTECT)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthProfile(models.Model):
    dni = models.CharField(unique=True, max_length=20)
    user = models.ForeignKey('AuthUser', unique=True, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'auth_profile'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.PROTECT)
    group = models.ForeignKey(AuthGroup, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.PROTECT)
    permission = models.ForeignKey(AuthPermission, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True, on_delete=models.PROTECT)
    user = models.ForeignKey(AuthUser, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'
