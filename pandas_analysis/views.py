from django.shortcuts import render
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
from django_pandas.io import read_frame
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, renderers, filters

# Create your views here.
#Pandas analysis  root
@api_view(['GET'])
def pandas_analysis_root(request, format = None):
   return Response({
      'papdata': reverse('pap-data', request = request, format = format),
      'papdata_download': reverse('pap-data-download', request = request, format = format),
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
    
    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')
    

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





