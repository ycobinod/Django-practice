from rest_framework import serializers


# class PublisherSerializer(serializers.Serializer):
#     name=serializers.CharField()
#     website=serializers.URLField()
#     email=serializers.EmailField()

# class BookSerializer(serializers.Serializer):
#     title=serializers.CharField()
#     publication_date=serializers.DateField()
#     isbn=serializers.CharField()
#     publisher=PublisherSerializer()

#class based view
# class PublisherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Publisher
#         fields=['name','website','email']

# class BookSerializer(serializers.ModelSerializer):
#     publisher=PublisherSerializer()
#     class Meta:
#         model=Book
#         fields=['title','publication_date','isbn','publisher']

    
from .models import Contributor

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contributor
        fields=['first_name','last_name','email']

