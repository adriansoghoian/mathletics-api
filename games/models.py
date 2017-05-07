from django.db import models
from django.conf import settings
# Create your models here.



class Game(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None)
	create_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)



