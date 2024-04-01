from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'hi',
            'why',
            'who',
            'where'
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
    

    def post(self, request):
        """Create a hello message with out name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({'message', message})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )
        

    def put(self, request, pk=None):
        """handling updates"""
        return Response({'method':'PUT'})
    

    def patch(self, request, pk=None):
        """handling partial updates"""
        return Response({'method':'PATCH'})
    

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        a_viewset = [
            'a','v','vv',
        ]

        return Response({'message':'hahaha','a_viewset':a_viewset})


    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    

    def retrieve(self, request, pk=None):
        """Handle getting by ID"""
        return Response({'method':'GET'})
    
    def update(self, request, pk=None):
        """Handle Updating by ID"""
        return Response({'method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle updating partially by ID"""
        return Response({'method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle deleting by ID"""
        return Response({'method':'DELETE'})