from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.PROTECT)
    dni = models.CharField(unique=True, max_length=20, default='0')
    
    class Meta:
        db_table = 'auth_profile'


@receiver(pre_save, sender=User)
def my_callback(sender, instance, * args, ** kwargs):
    instance.is_staff = 1
