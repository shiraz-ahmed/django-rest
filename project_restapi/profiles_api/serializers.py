from rest_framework import serializers


class api_serializer(serializers.Serializer):
    """ serializer is just like a form for the rest_api ,serialize the data and can validate  """
    name = serializers.CharField(max_length=15)
    email = serializers.EmailField(max_length=70)
