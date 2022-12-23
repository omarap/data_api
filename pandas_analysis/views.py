from api.models import *
from django.db.models import *
from pandas_analysis.serializers import *
from api.serializers import *
from rest_pandas import *
from rest_framework.renderers import *
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework_latex import renderers
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import renderers
import pandas as pd
import numpy as np
from django.core import serializers


# Create your views here.
#Pandas analysis  root
@api_view(['GET'])
def pandas_analysis_root(request, format = None):
   return Response({
      'papdata': reverse('pap-data', request = request, format = format),
      'papdata_download': reverse('pap-data-download', request = request, format = format),
      'pap_list_pdf': reverse('pap-list-pdf', request = request, format = format),
      'list_paps': reverse('list-paps', request = request, format = format),
      'construction_data_download': reverse('construction-data-download', request = request, format = format),
      'trees_data_download': reverse('trees-data-download', request = request, format = format),
      'crops_data_download': reverse('crops-data-download', request = request, format = format),
      'land_data_download': reverse('land-data-download', request = request, format = format)
   })

#JSON data for project affected person
class ProjectAffectedPersionJSONView(PandasView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProjectAffectedPerson.objects.all()
    serializer_class = ProjectAffectedPersonSerializer
    renderer_classes = [JSONOpenAPIRenderer]
    
    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')

#CSV file download for project affected person    
class ProjectAffectedPersionPandasView(PandasView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProjectAffectedPerson.objects.all()
    serializer_class = ProjectAffectedPersonSerializer
    renderer_classes = [PandasCSVRenderer, PandasExcelRenderer]
    
    def get_queryset(self, request):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')
    
    def get_data(self, request, *args, **kwargs):
        return ProjectAffectedPerson.objects.to_stats(
            index='created',
        )
    

    def get_pandas_filename(self, request, format):
        if format in ('xls', 'xlsx'):
            # Use custom filename and Content-Disposition header
            return "Data Export"  # Extension will be appended automatically
        else:
            # Default filename from URL (no Content-Disposition header)
            return None
 

#CSV file download for construction details    
class ConstructionPandasView(PandasView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ConstructionBuilding.objects.all()
    serializer_class = ConstructionBuildingSerializer
    renderer_classes = [PandasCSVRenderer, PandasExcelRenderer]
    
    def get_queryset(self):
        """
        This view should return a list of all the construction
        for the currently authenticated user.
        """
        owner = self.request.user
        return ConstructionBuilding.objects.filter(owner=owner).order_by('-created')
    

    def get_pandas_filename(self, request, format):
        if format in ('xls', 'xlsx'):
            # Use custom filename and Content-Disposition header
            return "Data Export"  # Extension will be appended automatically
        else:
            # Default filename from URL (no Content-Disposition header)
            return None


#CSV file download for Tree details    
class TreePandasView(PandasView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    renderer_classes = [PandasCSVRenderer, PandasExcelRenderer]
    
    def get_queryset(self):
        """
        This view should return a list of tress
        for the currently authenticated user.
        """
        owner = self.request.user
        return Tree.objects.filter(owner=owner).order_by('-created')
    

    def get_pandas_filename(self, request, format):
        if format in ('xls', 'xlsx'):
            # Use custom filename and Content-Disposition header
            return "Data Export"  # Extension will be appended automatically
        else:
            # Default filename from URL (no Content-Disposition header)
            return None


#CSV file download for crops   
class CropPandasView(PandasView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    renderer_classes = [PandasCSVRenderer, PandasExcelRenderer]
    
    def get_queryset(self):
        """
        This view should return a list of crops
        for the currently authenticated user.
        """
        owner = self.request.user
        return Crop.objects.filter(owner=owner).order_by('-created')
    

    def get_pandas_filename(self, request, format):
        if format in ('xls', 'xlsx'):
            # Use custom filename and Content-Disposition header
            return "Data Export"  # Extension will be appended automatically
        else:
            # Default filename from URL (no Content-Disposition header)
            return None

#CSV file download for land details    
class LandPandasView(PandasView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    renderer_classes = [PandasCSVRenderer, PandasExcelRenderer]
    
    def get_queryset(self):
        """
        This view should return a list of land
        for the currently authenticated user.
        """
        user = self.request.user
        return Land.objects.filter(user=user).order_by('-created')
    

    def get_pandas_filename(self, request, format):
        if format in ('xls', 'xlsx'):
            # Use custom filename and Content-Disposition header
            return "Data Export"  # Extension will be appended automatically
        else:
            # Default filename from URL (no Content-Disposition header)
            return None

#PDF Renderer class
class PDFRenderer(renderers.BaseRenderer):
    media_type = 'application/pdf'
    format = 'pdf'
    charset = None

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

#Project Affected Persions PDF view
class PAPListPDF(viewsets.ViewSet):
    renderer_classes = [ PDFRenderer ]

    def list(self, request):
        owner = self.request.user
        queryset = ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')
        serializer = ProjectAffectedPersonSerializer(queryset, many=True)
        response_dict = {serializer: 'serializer'}
        return Response(response_dict, status=200)
    
    def retrieve(self, request, pk=None):
        owner = self.request.user
        queryset = ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')
        pap = get_object_or_404(queryset, pk=pk)
        serializer = ProjectAffectedPersonSerializer(pap)
        response_dict = {serializer: 'serializer'}
        return Response(response_dict, status=200)

#Pandas API JSON Analysis
class ListPAPs(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProjectAffectedPerson.objects.all().order_by('-created')
    serializer_class = ProjectAffectedPersonSerializer
    
    try:
        def list(self, request, format=None):
            """
            This view should return a list of PAPs
            for the currently authenticated user.
            """
            owner = self.request.user
            pap_data = ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')
            df = pd.DataFrame(pap_data)
            pap_description = df.describe()
            return Response(pap_description)
    except ProjectAffectedPerson.DoesNotExist:
        raise Http404
    

