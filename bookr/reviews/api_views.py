from rest_framework import generics
from .models import Contributor
from  .serializers import ContributorSerializer

class ContributorView(generics.ListAPIView):
    queryset=Contributor.objects.all()
    serializer_class=ContributorSerializer