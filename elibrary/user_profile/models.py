# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=8)
    registration_number = models.CharField(max_length=8)
    hall_number = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(14)])
    room_number = models.PositiveIntegerField(default=0, validators=[MinValueValidator(101), MaxValueValidator(999)])
    mobile = PhoneNumberField(blank=False, null=False)
    email_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        managed = True


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

