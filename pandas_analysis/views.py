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
      'papdata_download': reverse('pap-data-download', request = request, format = format)
   })

class ProjectAffectedPersionJSONView(PandasView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProjectAffectedPerson.objects.all()
    serializer_class = ProjectAffectedPersionPandasSerializer
    pandas_serializer_class = PandasUnstackedSerializer
    renderer_classes = [JSONOpenAPIRenderer]
    
    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')
    

    
class ProjectAffectedPersionPandasView(PandasView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProjectAffectedPerson.objects.all()
    serializer_class = ProjectAffectedPersionPandasSerializer
    pandas_serializer_class = PandasUnstackedSerializer
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



    






    

