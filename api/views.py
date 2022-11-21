from django.shortcuts import render
from api.models import *
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, renderers, filters
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
import django_filters.rest_framework
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def api_root(request, format = None):
   return Response({
      'paps': reverse('pap-list', request = request, format = format),
      'land': reverse('land-list', request = request, format = format),
      'construction': reverse('construction-list', request = request, format = format),
      'trees': reverse('tree-list', request = request, format = format),
      'crops': reverse('crop-list', request = request, format = format)
   })


#projected affected person
class ProjectAffectedPersonList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProjectAffectedPerson.objects.all().order_by('-created')
    serializer_class = ProjectAffectedPersonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'id_no']


    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')
    
    def perform_create(self, serializer):
        owner = self.request.user
        #serializer holds a django model
        serializer.save(owner=owner)

#project affected person details with id
class ProjectAffectedPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProjectAffectedPerson.objects.all().order_by('-created')
    serializer_class = ProjectAffectedPersonSerializer


    def get_queryset(self):
        """
        This view should return a list of all the project_affected_person_details
        for the currently authenticated user.
        """
        owner = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')

#project affected person details with name
class ProjectAffectedPersonName(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProjectAffectedPerson.objects.all().order_by('-created')
    serializer_class = ProjectAffectedPersonSerializer

    try:
        def get(self, id_no):
            pap = ProjectAffectedPerson.objects.get(id_no=id_no)
            serializer = ProjectAffectedPersonSerializer(pap)
            return Response(serializer.data)
    except ProjectAffectedPerson.DoesNotExist:
            raise Http404

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_person_details
        for the currently authenticated user.
        """
        owner = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')

#Construction list
class ConstructionBuildingList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ConstructionBuilding.objects.all().order_by('name')
    serializer_class = ConstructionBuildingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return ConstructionBuilding.objects.filter(owner=owner).order_by('-rate')
    
    def perform_create(self, serializer):
        #serializer holds a django model
        serializer.save(owner=self.request.user)

#construction details for construction object with id
class ConstructionBuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ConstructionBuilding.objects.all().order_by('-rate')
    serializer_class = ConstructionBuildingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return ConstructionBuilding.objects.filter(owner=owner).order_by('-rate')

#construction details details with name
class ConstructionDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ConstructionBuilding.objects.all().order_by('-rate')
    serializer_class = ConstructionBuildingSerializer

    try:
        def get(self, name):
            construction = ConstructionBuilding.objects.get(name=name)
            serializer = ConstructionBuildingSerializer(construction)
            return Response(serializer.data)
    except ConstructionBuilding.DoesNotExist:
            raise Http404

    def get_queryset(self):
        """
        This view should return a list of all the construction details
        for the currently authenticated user.
        """
        owner = self.request.user
        return ConstructionBuilding.objects.filter(owner=owner).order_by('-created')

#Trees list
class TreeList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tree.objects.all().order_by('-rate')
    serializer_class = TreeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return Tree.objects.filter(owner=owner).order_by('-rate')

    def perform_create(self, serializer):
        owner = self.request.user
        #serializer holds a django model
        serializer.save(owner=owner)
    
#tree details for a tree    
class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tree.objects.all().order_by('-rate')
    serializer_class = TreeSerializer

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return Tree.objects.filter(owner=owner).order_by('-rate')

#Tree details details with name
class TreeDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tree.objects.all().order_by('-rate')
    serializer_class = TreeSerializer

    try:
        def trees(self, name):
            tree = Tree.objects.filter(name=name).order_by('-created')
            serializer = TreeSerializer(tree, many=True)
            return Response(serializer.data)
    except Tree.DoesNotExist:
            raise Http404

    def get_queryset(self):
        """
        This view should return tree details
        for the currently authenticated user.
        """
        owner = self.request.user
        return Tree.objects.filter(owner=owner).order_by('-created')



# Create your views here.
# Crop list
class CropList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Crop.objects.all().order_by('-rating')
    serializer_class = CropSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self):
        """
        This view should return a list of all the crop details
        for the currently authenticated user.
        """
        owner = self.request.user
        return Crop.objects.filter(owner=owner).order_by('-rating')

    def perform_create(self, serializer):
        #serializer holds a django model
        serializer.save(owner=self.request.user)

#crop details
class CropDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Crop.objects.all().order_by('-rating')
    serializer_class = CropSerializer

    def get_queryset(self):
        """
        This view should return a list of all the crop details
        for the currently authenticated user.
        """
        owner = self.request.user
        return Crop.objects.filter(owner=owner).order_by('-rating')

#crop details details with name
class CropDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

    try:
        def get(self, name):
            crop = Crop.objects.get(name=name)
            serializer = CropSerializer(crop)
            return Response(serializer.data)
    except Crop.DoesNotExist:
            raise Http404

    def get_queryset(self):
        """
        This view should return crop details
        for the currently authenticated user.
        """
        owner = self.request.user
        return Crop.objects.filter(owner=owner).order_by('-created')
        
#pap_crops
# ViewSets define the view behavior.
class PapCrop(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    """
    View to list all crops belonging to a pap in the system.
    """
    try:
        def get(self, request,first_name,format=None):
            pap = ProjectAffectedPerson.objects.get(first_name=first_name)
            pap_crops = Crop.objects.filter(pap=pap)
            serializer = CropSerializer(pap_crops, many=True)
            return Response(serializer.data)
    except Crop.DoesNotExist:
            raise Http404
    
    def get_queryset(self):
        """
        This view should return a list of all the paps
        for the currently authenticated user.
        """
        owner = self.request.user
        return ProjectAffectedPerson.objects.filter(owner=owner).order_by('-created')
    

#land list
class LandList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Land.objects.all().order_by('-rate')
    serializer_class = LandSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['land_type']

    def perform_create(self, serializer):
        user = self.request.user
        #serializer holds a django model
        serializer.save(user=user)

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_person land
        for the currently authenticated user.
        """
        user = self.request.user
        return Land.objects.filter(user=user).order_by('-rate')
    
#land details with id
class LandDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Land.objects.all().order_by('-rate')
    serializer_class = LandSerializer

#land details details with name
class LandDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Land.objects.all().order_by('-rate')
    serializer_class = ConstructionBuildingSerializer

    try:
        def get(self, land_type):
            land = Land.objects.get(land_type=land_type)
            serializer = LandSerializer(land)
            return Response(serializer.data)
    except Land.DoesNotExist:
            raise Http404

    def get_queryset(self):
        """
        This view should return land details
        for the currently authenticated user.
        """
        owner = self.request.user
        return Land.objects.filter(owner=owner).order_by('-created')

#pap_land
# ViewSets define the view behavior.
class PapLandView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['land_type']
    """
    View to list all land belonging to a particular pap.
    """
    try:
        def get(self, request,first_name,format=None):
            pap = ProjectAffectedPerson.objects.get(first_name=first_name)
            pap_land = Land.objects.filter(pap=pap).order_by('-rate')
            serializer = LandSerializer(pap_land, many=True)
            return Response(serializer.data)
    except Land.DoesNotExist:
            raise Http404
    
    def get_queryset(self):
        """
        This view should return a list of all the paps
        for the currently authenticated user.
        """
        owner = self.request.user
        return Land.objects.filter(owner=owner).order_by('-rate')

#pap_trees
# ViewSets define the view behavior.
class PapTreeView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    """
    View to list all trees belonging to a particular pap.
    """
    try:
        def get(self, first_name):
            pap = ProjectAffectedPerson.objects.get(first_name=first_name)
            pap_trees = Tree.objects.filter(pap=pap).order_by('-created')
            serializer = TreeSerializer(pap_trees, many=True)
            return Response(serializer.data)
    except Tree.DoesNotExist:
            raise Http404
    
    def get_queryset(self):
        """
        This view should return a list of all the paps
        for the currently authenticated user.
        """
        owner = self.request.user
        return Tree.objects.filter(owner=owner).order_by('-created')

#pap_construction
# ViewSets define the view behavior.
class PapConstructionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['-created']
    """
    View to list all construction belonging to a particular pap.
    """
    try:
        def get(self, request,first_name,format=None):
            pap = ProjectAffectedPerson.objects.get(first_name=first_name)
            pap_construction = ConstructionBuilding.objects.filter(pap=pap).order_by('-rate')
            serializer = ConstructionBuildingSerializer(pap_construction, many=True)
            return Response(serializer.data)
    except ConstructionBuilding.DoesNotExist:
            raise Http404
    
    def get_queryset(self):
        """
        This view should return a list of all the paps
        for the currently authenticated user.
        """
        owner = self.request.user
        return ConstructionBuilding.objects.filter(owner=owner).order_by('-rate')
    




