# -*- coding: utf-8 -*-
from mantenimiento.models import Materiales , GeneralDetalle, UnidadMedida , Proyectos
from django import forms

class MaterialesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MaterialesForm, self).__init__(*args, **kwargs)
        self.fields['id_codTipoGasto'].queryset = GeneralDetalle.objects.filter(id_general=6, b_flagInactivo = 0).order_by('vc_valor1')
        self.fields['id_codFamilia'].queryset = GeneralDetalle.objects.filter(id_general=11 , b_flagInactivo = 0).order_by('vc_valor1')
        self.fields['id_codClasificacion'].queryset = GeneralDetalle.objects.filter(id_general=12 , b_flagInactivo = 0).order_by('vc_valor1')
        self.fields['id_codColor'].queryset = GeneralDetalle.objects.filter(id_general=13, b_flagInactivo = 0 ).order_by('vc_valor1')
        self.fields['id_unidadMedida'].queryset = UnidadMedida.objects.filter(b_flagInactivo=0)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            instance = getattr(self, 'instance', None)

    class Meta:
        model = Materiales
        fields = ('vc_codigo', 'id_codTipoGasto' , 'id_codFamilia' , 'id_codClasificacion', 'vc_descripcion',
                  'id_codColor' , 'nu_valor' , 'id_unidadMedida' , 'nu_stockMinimo' , 'nu_stockMaximo', 'nu_stockActual')
        widgets = {
            'vc_codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'id_codTipoGasto': forms.Select(attrs={'class': 'form-control'}),
            'id_codFamilia': forms.Select(attrs={'class': 'form-control'}),
            'id_codClasificacion': forms.Select(attrs={'class': 'form-control'}),
            'vc_descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_codColor': forms.Select(attrs={'class': 'form-control' , 'onChange' : 'selectColor(this.value)'}),
            'nu_valor': forms.TextInput(attrs={'class': 'form-control', 'style' : 'text-align:right'}),
            'id_unidadMedida': forms.Select(attrs={'class': 'form-control'}),
            'nu_stockMinimo': forms.TextInput(attrs={'class': 'form-control text-rigth', 'style' : 'text-align:right'}),
            'nu_stockMaximo': forms.TextInput(attrs={'class': 'form-control text-rigth', 'style' : 'text-align:right'}),
            'nu_stockActual': forms.TextInput(attrs={'class': 'form-control text-rigth', 'style' : 'text-align:right' , 'readonly' : 'readonly'}),
        }
        labels = {
            'vc_codigo': 'Código',
            'id_codTipoGasto': 'Tipo de Gasto',
            'id_codFamilia': 'Familia',
            'id_codClasificacion': 'Clasificación',
            'vc_descripcion': 'Descripción',
            'id_codColor': 'Color',
            'nu_valor': 'Valor',
            'id_unidadMedida': 'Uni. Med',
            'nu_stockMinimo': 'Stock Min',
            'nu_stockMaximo': 'Stock Max',
            'nu_stockActual': 'Stock Actual'
        }

# class ProyectosForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ProyectosForm, self).__init__(*args, **kwargs)
#         self.fields['id_codTipoGasto'].queryset = GeneralDetalle.objects.filter(id_general=6, b_flagInactivo = 0)
#         self.fields['id_codFamilia'].queryset = GeneralDetalle.objects.filter(id_general=11 , b_flagInactivo = 0).order_by('vc_valor1')
#         self.fields['id_codClasificacion'].queryset = GeneralDetalle.objects.filter(id_general=12 , b_flagInactivo = 0).order_by('vc_valor1')
#         self.fields['id_codColor'].queryset = GeneralDetalle.objects.filter(id_general=13, b_flagInactivo = 0 ).order_by('vc_valor1')
#         self.fields['id_unidadMedida'].queryset = UnidadMedida.objects.filter(b_flagInactivo=0)

#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
#             instance = getattr(self, 'instance', None)

#     class Meta:
#         model = Materiales
#         fields = ('vc_nombreProyecto', 'id_ubigeo' , 'vc_direccion' , 'dt_fecAprobacion', 'dt_fecInicio',
#                   'dt_fecCierre' , 'id_colaborador' , 'vc_nomContacto' , 'vc_telfContacto' , 'id_cliente')
#         widgets = {
#             'vc_nombreProyecto': forms.TextInput(attrs={'class': 'form-control'}),
#             'id_ubigeo': forms.Select(attrs={'class': 'form-control'}),
#             'vc_direccion': forms.Select(attrs={'class': 'form-control'}),
#             'dt_fecAprobacion': forms.Select(attrs={'class': 'form-control'}),
#             'dt_fecInicio': forms.TextInput(attrs={'class': 'form-control'}),
#             'dt_fecCierre': forms.Select(attrs={'class': 'form-control' }),
#             'id_colaborador': forms.TextInput(attrs={'class': 'form-control'}),
#             'vc_nomContacto': forms.Select(attrs={'class': 'form-control'}),
#             'vc_telfContacto': forms.TextInput(attrs={'class': 'form-control '}),
#             'id_cliente': forms.TextInput(attrs={'class': 'form-control'}),
#         }
#         labels = {
#             'vc_nombreProyecto': 'Nom. Proyecto',
#             'id_ubigeo': 'Distrito del Proyecto',
#             'vc_direccion': 'Dirección del Proyecto',
#             'dt_fecAprobacion': 'Fecha Aprobación',
#             'dt_fecInicio': 'Fecha Inicio',
#             'dt_fecCierre': 'Fecha Cierre',
#             'id_colaborador': 'Supervisor de Obra',
#             'vc_nomContacto': 'Contacto',
#             'vc_telfContacto': 'Tel. Cntacto',
#             'id_cliente': 'Stock Max'
#         }


class GeneralDetalleForm(forms.ModelForm):
        
    class Meta:
        model = GeneralDetalle
        fields = ('vc_valor1',)
        widgets = {'vc_valor1' : forms.TextInput(attrs={'class': 'form-control'}),}
        labels = {
            'vc_valor1': 'Código'
        }