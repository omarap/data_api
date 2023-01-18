from rest_framework import serializers
from rest_framework import *
from .models import *
from django.core.serializers import serialize
from django.db.models import Sum
from django.db import models


#function to limit paps to current user i.e. pap owner or view only your created paps
class UserPapForeignKey(serializers.SlugRelatedField):
    def get_queryset(self):
        pap = ProjectAffectedPerson.objects.filter(owner = self.context.get("request").user).order_by('-created')[:6]
        return pap

class ConstructionListSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = ConstructionList
        fields =['name', 'created', 'updated']
    
    def create(self, validated_data):
        """
        Create and return a new `ConstructionList` instance, given the validated data.
        """
        return ConstructionList.objects.create(**validated_data)

class ConstructionBuildingSerializer(serializers.ModelSerializer):
    pap = serializers.SlugRelatedField(
        slug_field='first_name',
        queryset=ProjectAffectedPerson.objects.all()
    )
    name = serializers.SlugRelatedField(
        slug_field='name',
        queryset=ConstructionList.objects.all()
    )
    
    class Meta:
        model = ConstructionBuilding
        fields = ['pap', 'name','construction_image', 'size', 'number_of_construction','rate', 'value_of_structures','created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new `Crop` instance, given the validated data.
        """
        return ConstructionBuilding.objects.create(**validated_data)


class CropListSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = CropList
        fields =['name', 'rate', 'district', 'created', 'updated']
    
    def create(self, validated_data):
        """
        Create and return a new `CropList` instance, given the validated data.
        """
        return CropList.objects.create(**validated_data)


class CropSerializer(serializers.ModelSerializer):
    pap = serializers.SlugRelatedField(
        slug_field='first_name',
        queryset=ProjectAffectedPerson.objects.all()

    )
    crop_name = serializers.SlugRelatedField(
        slug_field='name',
        queryset=CropList.objects.all()

    )
    class Meta:
        model = Crop
        fields = ['crop_name', 'crop_image','description', 'quantity', 'quality', 'rate',
        'pap','value_of_crops','created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new `Crop` instance, given the validated data.
        """
        return Crop.objects.create(**validated_data)

class LandListSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = LandList
        fields =['name', 'created', 'updated']
    
    def create(self, validated_data):
        """
        Create and return a new `LandList` instance, given the validated data.
        """
        return LandList.objects.create(**validated_data)

class TenureTypeSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = TenureType
        fields =['name','created', 'updated']
    
    def create(self, validated_data):
        """
        Create and return a new `Tenure Type` instance, given the validated data.
        """
        return TenureType.objects.create(**validated_data)

class LandSerializer(serializers.ModelSerializer):
    pap = serializers.SlugRelatedField(
        slug_field='first_name',
        queryset=ProjectAffectedPerson.objects.all()
    )
    land_type = serializers.SlugRelatedField(
        slug_field='name',
        queryset=LandList.objects.all()
    )
    tenure = serializers.SlugRelatedField(
        slug_field='name',
        queryset=TenureType.objects.all()
    )

    class Meta:
        model = Land
        fields = ['land_type', 'land_image','survey_no', 'pap','tenure', 'size', 'location', 'land_use', 
                    'land_services', 'rate','value_of_land', 'created', 'updated']

class TreeListSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = TreeList
        fields =['name', 'rate', 'district', 'created', 'updated']
    
    def create(self, validated_data):
        """
        Create and return a new `TreeList` instance, given the validated data.
        """
        return TreeList.objects.create(**validated_data)

class TreeSerializer(serializers.ModelSerializer):
    pap = serializers.SlugRelatedField(
        slug_field='first_name',
        queryset=ProjectAffectedPerson.objects.all()
    )
    name = serializers.SlugRelatedField(
        slug_field='name',
        queryset=TreeList.objects.all()
    )
    
    class Meta:
        model = Tree
        fields = ['pap', 'name', 'description','tree_image', 'quantity','rate', 'value_of_trees', 'created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new `Tree` instance, given the validated data.
        """
        Tree.objects.create(**validated_data)

    
class ProjectAffectedPersonSerializer(serializers.ModelSerializer):
    pap_crops = CropSerializer(many=True, read_only=True)
    pap_lands = LandSerializer(many=True, read_only=True)
    pap_construction= ConstructionBuildingSerializer(many=True, read_only=True)
    pap_trees= TreeSerializer(many=True, read_only=True)
    class Meta:
        model = ProjectAffectedPerson
        fields = ['id','first_name', 'last_name', 'pap_image','age', 'address', 
        'nin','email','phone_number','pap_crops','pap_lands','pap_trees',
        'pap_construction','created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new `ProjectAffectedPerson` instance, given the validated data.
        """
        return ProjectAffectedPerson.objects.create(**validated_data)


#CSV FILES UPLOADS
#CSV File Uploads
class FileUploadSerializer(serializers.Serializer):
        file = serializers.FileField()

class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = ProjectAffectedPerson
        fields = fields = ['id','first_name', 'last_name', 'pap_image','age', 'address', 
        'nin','email','phone_number']


#CROPS CSV Uploads
class CropUploadSerializer(serializers.Serializer):
        file = serializers.FileField()

class SaveCropFileSerializer(serializers.Serializer):
    
    class Meta:
        model = CropList
        fields =  fields =['name', 'rate', 'district']

#LAND LIST NAMES CSV Uploads
class LandUploadSerializer(serializers.Serializer):
        file = serializers.FileField()

class SaveLandFileSerializer(serializers.Serializer):
    
    class Meta:
        model = LandList
        fields =  fields =['name']

#LAND TUNURE NAMES CSV Uploads
class TenureTypeUploadSerializer(serializers.Serializer):
        file = serializers.FileField()

class SaveTenureTypeFileSerializer(serializers.Serializer):
    
    class Meta:
        model = TenureType
        fields =  fields =['name']

#Construction Names CSV Uploads
class ConstructionNameListUploadSerializer(serializers.Serializer):
        file = serializers.FileField()

class SaveConstructionNameListFileSerializer(serializers.Serializer):
    
    class Meta:
        model = ConstructionList
        fields =  fields =['name']

#TREES CSV Uploads
class TreeUploadSerializer(serializers.Serializer):
        file = serializers.FileField()

class SaveTreeFileSerializer(serializers.Serializer):
    
    class Meta:
        model = TreeList
        fields =  fields =['name', 'rate', 'district']
    
    
    
    
    


    
