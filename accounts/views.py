# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import PasswordResetFormCustom
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from django.contrib.auth import logout 
from django.shortcuts import redirect
#from django.urls import reverse_lazy
from django.core.urlresolvers import reverse_lazy

class HomeView(generic.TemplateView):
    template_name = "accounts-home.html"
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))
        

class UserListView(generic.ListView):
    model = User
    template_name = 'accounts-index.html'  # Specify your own template name/location

    
    def get_queryset(self):
        return User.objects.exclude(first_name='', last_name='')
    
    def get_context_data(self, ** kwargs):
        context = super(UserListView, self).get_context_data(** kwargs)
        return context
    

class UserResetPassword(View):
    form_class = PasswordResetFormCustom
    template_name = 'password_reset_form.html'
    
    def get(self, request, * args, ** kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, * args, ** kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data.get('username'), profile__dni=form.cleaned_data.get('dni'))
                email = user.email
                formreset = PasswordResetForm({'email': email})
                assert formreset.is_valid()
                formreset.save(
                               request=request,
                               email_template_name='registration/password_reset_email.html',
                               html_email_template_name='password_reset_email.html')
                return render(request, 'password_reset_done.html', {"email" : user.email , 'user' : form.cleaned_data.get('username') })
            except User.DoesNotExist:
                return render(request, self.template_name, {'form': form, 'messages': ('Usuario o DNI incorrecto',)})
           
        return render(request, self.template_name, {'form': form})