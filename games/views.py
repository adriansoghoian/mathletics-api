from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, authentication, permissions, viewsets, mixins
from rest_framework.renderers import JSONRenderer

from games.models import Game, Statistics, GAME_TYPE



class Games(APIView):
	"""
	General game endpoint. 

	"""
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (authentication.TokenAuthentication,)


	def get(self, request, format=None):
		print "Games GET"
		print request.data
		return Response(None, status=status.HTTP_200_OK)


	def post(self, request, format=None):
		print "Games POST"
		print request.data

		return Response(None, status=status.HTTP_200_OK)





class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)