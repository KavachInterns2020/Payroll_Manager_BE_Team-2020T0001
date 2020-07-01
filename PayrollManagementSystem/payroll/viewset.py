from rest_framework import viewsets
from . import models, serializers


class CompanyViewset(viewsets.ModelViewSet):
    queryset = models.Companies.objects.all()
    serializer_class = serializers.CompanySerializer

