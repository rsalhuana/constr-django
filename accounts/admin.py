# -*- coding: utf-8 -*-
from .models import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

admin.site.unregister(User)
    
class EmailRequiredMixin(object):
    def __init__(self, * args, ** kwargs):
        super(EmailRequiredMixin, self).__init__(*args, ** kwargs)
        self.fields['email'].required = True
        
class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
    pass


class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
    pass

class UserProfileInline(admin.StackedInline):
    model = Profile

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline,] 
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    add_fieldsets = ((None, {'fields': ('username', 'email',
                     'password1', 'password2'), 'classes': ('wide', )}), )


admin.site.register(User, UserProfileAdmin)