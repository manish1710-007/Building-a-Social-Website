from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, 
                              on_delete=models.CASCADE)
  date_of_birth = models.DateTimeField(blank=True, null=True)
  photo = models.ImageField(upload_to='users/%y/%m/%m/',
                                                        blank=True)

  def __str__(self):
    return "Profile for user {}".format(self.user.username)                                                      
