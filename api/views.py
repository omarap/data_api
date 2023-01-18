from django.shortcuts import render
from api.models import *
from api.serializers import *
from rest_framework.renderers import *
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, renderers, filters
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
import django_filters.rest_framework
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import *
from rest_framework import status
import io, csv, pandas as pd

@api_view(['GET'])
def api_root(request, format = None):
   return Response({
      'paps': reverse('pap-list', request = request, format = format),
      'land': reverse('land-list', request = request, format = format),
      'construction': reverse('construction-list', request = request, format = format),
      'trees': reverse('tree-list', request = request, format = format),
      'crops': reverse('crop-list', request = request, format = format),
      'addcrops': reverse('crop-list-names', request = request, format = format),
      'upload_pap_csv_file': reverse('upload-pap-file-csv', request = request, format = format),
      'upload_crops_csv_file': reverse('upload-crop-file-csv', request = request, format = format)
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
class ProjectAffectedPersonNameView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProjectAffectedPerson.objects.all().order_by('-created')
    serializer_class = ProjectAffectedPersonSerializer

    try:
        def list(self, request, first_name):
            pap = ProjectAffectedPerson.objects.get(first_name=first_name)
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

#Construction list names
class ConstructionListName(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ConstructionList.objects.all().order_by('-created')
    serializer_class = ConstructionListSerialier
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def perform_create(self, serializer):
        owner = self.request.user
        #serializer holds a django model
        serializer.save(owner=owner)
        
#crop details
class ConstructionListDetailName(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ConstructionList.objects.all().order_by('-created')
    serializer_class = ConstructionListSerialier
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    
#list of constructions
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
        owner = self.request.user
        pap = ProjectAffectedPerson.objects.filter(owner=owner)        #serializer holds a django model
        serializer.save(owner=owner, pap=pap)



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
class ConstructionDetailNameView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ConstructionBuilding.objects.all().order_by('-rate')
    serializer_class = ConstructionBuildingSerializer

    try:
        def list(self, request, name):
            construction = ConstructionBuilding.objects.filter(name=name)
            serializer = ConstructionBuildingSerializer(construction, many=True)
            return Response(serializer.data)
    except ConstructionBuilding.DoesNotExist:
            raise Http404

    #count number of construction names
    try:
        def count_construction(self, request,name):
            construction_count = ConstructionBuilding.objects.filter(name=name).order_by('-created').aggregate(Count('name'))
            return Response(construction_count)
    except ConstructionBuilding.DoesNotExist:
            raise Http404
            
    
    def get_queryset(self):
        """
        This view should return a list of all the construction details
        for the currently authenticated user.
        """
        owner = self.request.user
        return ConstructionBuilding.objects.filter(owner=owner).order_by('-created')

#tree list names
class TreeListName(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TreeList.objects.all().order_by('-created')
    serializer_class = TreeListSerialier
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def perform_create(self, serializer):
        owner = self.request.user
        #serializer holds a django model
        serializer.save(owner=owner)
        
#tree details name
class TreeListDetailName(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TreeList.objects.all().order_by('-created')
    serializer_class = TreeListSerialier
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

#list of trees
class TreeList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tree.objects.all().order_by('-rate')
    serializer_class = TreeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def perform_create(self, request, serializer):
        owner = self.request.user
        request = request.user
        serializer = TreeSerializer(data=request.data)
        #serializer holds a django model
        serializer.save(owner=owner)

    def get_queryset(self):
        """
        This view should return a list of all the project_affected_persons
        for the currently authenticated user.
        """
        owner = self.request.user
        return Tree.objects.filter(owner=owner).order_by('-rate')

   
    
#tree details  
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
class TreeDetailNameView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tree.objects.all().order_by('-rate')
    serializer_class = TreeSerializer
    #tree details details with name
    try:
        def list(self, request, name):
            tree = Tree.objects.filter(name=name).order_by('-created')
            serializer = TreeSerializer(tree, many=True)
            return Response(serializer.data)
    except Tree.DoesNotExist:
            raise Http404

    #count number of tree names
    try:
        def count_tree(self, request,name):
            trees_count = Tree.objects.filter(name=name).order_by('-created').aggregate(Count('name'))
            return Response(trees_count)
    except Tree.DoesNotExist:
            raise Http404
            

    def get_queryset(self):
        """
        This view should return tree details
        for the currently authenticated user.
        """
        owner = self.request.user
        return Tree.objects.filter(owner=owner).order_by('-created')

#Crop list names and rate
class CropListName(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CropList.objects.all().order_by('-created')
    serializer_class = CropListSerialier
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'district']
    

    def perform_create(self, serializer):
        owner = self.request.user
        #serializer holds a django model
        serializer.save(owner=owner)
        

#crop details
class CropListDetailName(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CropList.objects.all().order_by('-created')
    serializer_class = CropListSerialier
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'district']

    

# Create your views here.
# Crop list
class CropList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Crop.objects.all().order_by('-created')
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
        return Crop.objects.filter(owner=owner).order_by('-created')

    def perform_create(self, serializer):
        owner = self.request.user
        #serializer holds a django model
        serializer.save(owner=owner)

#crop details
class CropDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Crop.objects.all().order_by('-created')
    serializer_class = CropSerializer

    def get_queryset(self):
        """
        This view should return a list of all the crop details
        for the currently authenticated user.
        """
        owner = self.request.user
        return Crop.objects.filter(owner=owner).order_by('-created')

#crop details details with name
class CropDetailNameView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

    try:
        def list(self,request, name):
            crop = Crop.objects.filter(name=name)
            serializer = CropSerializer(crop, many=True)
            return Response(serializer.data)
    except Crop.DoesNotExist:
            raise Http404

    #count number of crop names
    try:
        def count_crops(self, request,name):
            crops_count = Crop.objects.filter(name=name).order_by('-created').aggregate(Count('name'))
            return Response(crops_count)
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
class PapCrop(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    """
    View to list all crops belonging to a pap in the system.
    """
    try:
        def list(self, request, first_name):
            pap = ProjectAffectedPerson.objects.get(first_name=first_name)
            pap_crops = Crop.objects.filter(pap=pap).order_by('-created')
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
    
#land list names
class LandListName(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = LandList.objects.all().order_by('-created')
    serializer_class = LandListSerialier
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def perform_create(self, serializer):
        owner = self.request.user
        #serializer holds a django model
        serializer.save(owner=owner)
        
#land details name
class LandListDetailName(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = LandList.objects.all().order_by('-created')
    serializer_class = LandListSerialier
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

#list of land
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
class LandDetailNameView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Land.objects.all().order_by('-rate')
    serializer_class = ConstructionBuildingSerializer

    try:
        def list(self, request, land_type):
            land = Land.objects.filter(land_type=land_type)
            serializer = LandSerializer(land, many=True)
            return Response(serializer.data)
    except Land.DoesNotExist:
            raise Http404
    
    #count number of land names
    try:
        def count_land(self, request,name):
            land_count = Land.objects.filter(name=name).order_by('-created').aggregate(Count('name'))
            return Response(land_count)
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
class PapLandView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['land_type']
    """
    View to list all land belonging to a particular pap.
    """
    try:
        def list(self, request,first_name,format=None):
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
        user = self.request.user
        return Land.objects.filter(user=user).order_by('-rate')

#pap_trees
# ViewSets define the view behavior.
class PapTreeView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    """
    View to list all trees belonging to a particular pap.
    """
    try:
        def list(self, request, first_name):
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
class PapConstructionView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['-created']
    """
    View to list all construction belonging to a particular pap.
    """
    try:
        def list(self, request,first_name,format=None):
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
    

#CSV FILE UPLOADS
class UploadFileView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileUploadSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = ProjectAffectedPerson(
                       id = row['id'],
                       first_name= row["first_name"],
                       last_name= row['last_name'],
                       age= row["age"],
                       address= row["address"],
                       id_no= row["id_no"],
                       email= row["email"],
                       phone_number= row["phone_number"]
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)


#Crop CSV FILE UPLOADS
class UploadCropFileView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CropUploadSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = CropList(
                       name= row["name"],
                       rate= row['rate'],
                       district= row["district"]
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

