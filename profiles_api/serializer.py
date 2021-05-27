from rest_framework import serializers
#covert data input to python object and vice versa

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)