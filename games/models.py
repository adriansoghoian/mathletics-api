from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


GAME_TYPE = [("Multiplication 60","multiplication_60"),]


class Game(models.Model):
	user = models.ForeignKey(User, default=None)
	create_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	game_type = models.CharField(max_length=200, choices=GAME_TYPE)



class Statistics(models.Model):
	game = models.ForeignKey(Game)
	create_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	start_time =  models.DateTimeField(default=None)
	end_time = models.DateTimeField(default=None)
	number_correct = models.IntegerField(default=None)
	number_incorrect = models.IntegerField(default=None)





