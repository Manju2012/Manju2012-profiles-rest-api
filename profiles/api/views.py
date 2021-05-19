from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from . import serializers


class HelloApiView(APIView):
    """Test API View """
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """returns a list of APIview features"""

        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you most control over apps logic ',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """craete a heloo message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle Delete of an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API view sets"""

    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """return Hello message"""

        a_viewsets = [
            'Uses action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more funcs with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewsets})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            Response(serializer.errors,
                     status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'DELETE'})
