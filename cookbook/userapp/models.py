from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class BookUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)
    # profile = models.ForeignKey(Profile, blank=True, related_name='profile')

    # Переопределение метода save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Создаем профиль
        # Если профиль не создан
        if not Profile.objects.filter(user=self).exists():
            Profile.objects.create(user=self)

class Profile(models.Model):
    # При создании пользователя создать Profile
    info = models.TextField(blank=True)
    user = models.OneToOneField(BookUser, on_delete=models.CASCADE)



# @receiver(post_save, sender=BlogUser)
# def create_profile(sender, instance, **kwargs):
#     print('Сработал обработчик сигнала')
#     if not Profile.objects.filter(user=instance).exists():
#         Profile.objects.create(user=instance)
