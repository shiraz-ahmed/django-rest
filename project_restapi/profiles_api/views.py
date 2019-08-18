from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import api_serializer,userprofile_serializer,profilefeed_item_serializer
from rest_framework import viewsets
from .models import userprofile,profilefeed_item
from rest_framework.authentication import TokenAuthentication
from .permissions import update_own_profile,update_own_status
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated







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


class api_viewsets(viewsets.ViewSet):
    """the above method used is similar to that one with an exception of the listview,updateview,destroy view"""
    serializer_class = api_serializer
    def list(self,request):
        """request a list view"""
        a_viewset=[
        'provide more functionality in less code ',
        'automatically maps to urls using routers',
        'uses functions like (list,create,retrieve,update,partial_update,destroy)'
        ]

        return Response({'message':'this is the listview','view':a_viewset
        })

    def create(self,request):
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

    def retrieve(self,request,pk=None):
        return Response({'http method':'GET'})

    def update(self,request,pk=None):
        return Response({'http method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http method':'patch'})

    def destroy(self,request,pk=None):
        return Response({'http method':'delete'})


class userprofile_viewset(viewsets.ModelViewSet):
    """model view is for the managing the database and connecting api to the serializers ."""
    serializer_class = userprofile_serializer
    queryset=userprofile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(update_own_profile,)
    # making a search ,dont forget to put the comma after the permissions_classes varialbes  b/c it must be considered as tuple not a single object
    filter_backends=(filters.SearchFilter,) #dont forget to put comma
    search_fields=('name','email',)



class user_login_apiview(ObtainAuthToken):

    """an api for user login"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class userprofile_feed_viewset(viewsets.ModelViewSet):
    """create update,delete for profilefeed_item."""
    authentication_classes=(TokenAuthentication,)
    serializer_class=profilefeed_item_serializer
    queryset=profilefeed_item.objects.all()
    permission_classes=(update_own_status,IsAuthenticated)
    # IsAuthenticatedOrReadOnly is used when we are not authenitcated but still we can read the content,is uathemticated mwan we read when we are loged in
    def perform_create(self,serializer): #when the user is authenitcated it gets added to the database
        serializer.save(user_profile=self.request.user)
