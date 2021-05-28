from profiles_api import serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializer.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    def post(self,request):
        """create hallo messgae with name""" 
        #self.serializer_class comes with the framework
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'hello {(name)}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)#400 integer could have been used but to ensure the understanding we used the full bad request
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})
    def delete(self, request, pk=None):
         """Delete an object"""
         return Response({'method': 'DELETE'})        
    # put updates the object fully
    # put updates the object partially, means update the object partially only thr required part is changed
             

