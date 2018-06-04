# -*- coding: utf-8 -*-
from .models import Proyectos , GeneralDetalle , Ubigeo, Colaborador
from django import forms

class ProyectosForm(forms.ModelForm):

    class Meta:
        model = Proyectos
        documento = GeneralDetalle.objects.filter(id_general= 8)
        ubigeo = Ubigeo.objects.all()
        colaborador = Colaborador.objects.all()
        fields = ('vc_codTipoDocumento' , 'vc_numDocumento' , 'vc_nombreProyecto' , 'id_ubigeo', 'vc_direccion',
                  'dt_fecAprobacion' , 'dt_fecInicio' , 'dt_fecCierre' , 'id_colaborador' , 'vc_nomContacto' , 'vc_telfContacto',
                  'dt_crea')
        widgets = {
         #   'vc_codEstado': forms.TextInput(attrs={'class': 'form-control' , 'value' : 16 } ),
            # 'vc_codEstado': forms.Select(choices=( (edo.id_generalDetalle, edo.vc_valor1) for edo in estado ) , attrs={'class': 'form-control'}),
            'vc_codTipoDocumento': forms.Select(choices=( (doc.id_generalDetalle, doc.vc_valor1) for doc in documento ) , attrs={'class': 'form-control'}),
            'vc_numDocumento': forms.TextInput(attrs={'class': 'form-control'}),
            'vc_nombreProyecto': forms.TextInput(attrs={'class': 'form-control'}),
            'id_ubigeo': forms.Select(choices=( (ubig.id_ubigeo, ubig.vc_descripcion) for ubig in ubigeo ) , attrs={'class': 'form-control'}),
            'vc_direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_fecAprobacion': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_fecInicio': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_fecCierre': forms.TextInput(attrs={'class': 'form-control'}),
            'id_colaborador': forms.Select(choices=( (col.id_colaborador, col.vc_nomColaborador, col.vc_apePatColaborador) for col in colaborador ) , attrs={'class': 'form-control'}),
            'vc_nomContacto': forms.TextInput(attrs={'class': 'form-control'}),
            'vc_telfContacto': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_crea': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            # 'vc_codEstado': 'Estado',
            'vc_codTipoDocumento': 'Tipo de Documento',
            'vc_numDocumento': 'Número de Documento',
            'vc_nombreProyecto': 'Nombre del Proyecto',
            'id_ubigeo': 'Distrito Proyecto',
            'vc_direccion': 'Direccion del Proyecto',
            'dt_fecAprobacion': 'Fecha Aprobación',
            'dt_fecInicio': 'Fecha Inicio',
            'dt_fecCierre': 'Fecha Cierre',
            'id_colaborador': 'Supervisor de Obra',
            'vc_nomContacto': 'Contacto',
            'vc_telfContacto': 'Telefono Contacto'
        }