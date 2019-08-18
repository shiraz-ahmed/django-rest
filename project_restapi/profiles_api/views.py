from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import api_serializer
# Create your views here.
class my_api(APIView):
    """Using rest_framework api for crud system"""
    serializer_class = api_serializer
    def get(self,request,format=None):
        def_api=[
        'this is same as django view',
        'gives more control over the logic',
        'uses http method as functions like (get,put,post,patch,delete)',
        'mapped manually to the URLs',
        ]
        return Response({'message':'my message is hellow world','def_api':def_api})


    def post(self,request):
        """create a hellow world message with the post method """
        serializer= self.serializer_class(data=request.data) #POST DATA will go to the serializer once we done with that then we can perform new functions
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            message=f'Hellow {name}'
            return Response({'message':message,'email entered was ':email})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


    def put(self,request,pk=None):
        return Response({'method used':'PUT'})


    def patch(self,request,pk=None):
        """ the difference b/w put and patch is that it partially updates the data ,the only fields we want to update ,like in
        case of first name last name we want to update last name so we use patch if we use put it will completely overwrite the name """
        return Response({'method used':'PATCH'})


    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method used':'DELETE'})
