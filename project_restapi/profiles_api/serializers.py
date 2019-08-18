from rest_framework import serializers
from .models import userprofile

class api_serializer(serializers.Serializer):
    """ serializer is just like a form for the rest_api ,serialize the data and can validate  """
    name = serializers.CharField(max_length=15)
    email = serializers.EmailField(max_length=70)



class userprofile_serializer(serializers.ModelSerializer):
    """docstring fo userprofile_serializer."""
    class Meta:
        model =userprofile
        fields=('id','name','email','password')
        extra_kwargs={
        'password':{
        'write_only':True, #this is it can be used for post not for get method
        'style':{'input_type':'password'} #the usual password type look
        }
        }

    def create(self,validated_data):
        # create and return a new usermodel,create_user function is from the userprofile_manager

        user=userprofile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password'],

        )
        return user
