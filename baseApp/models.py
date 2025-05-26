from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):

    def __str__(self):
        return '{} - {} {}'.format(self.username, self.first_name, self.last_name)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name = 'user_profile', on_delete= models.PROTECT)
    interest = models.TextField(blank=True)
    birth = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return '{}'.format(self.user.username)