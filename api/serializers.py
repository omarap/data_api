from rest_framework import serializers
from rest_framework import *
from .models import *

#function to limit paps to current user i.e. pap owner or view only your created paps
class UserPapForeignKey(serializers.SlugRelatedField):
    def get_queryset(self):
        return ProjectAffectedPerson.objects.filter(owner =  self.context['request'].user).order_by('-created')[:6]

class ConstructionBuildingSerializer(serializers.ModelSerializer):
    pap = UserPapForeignKey(
        slug_field='first_name'
    )
    
    class Meta:
        model = ConstructionBuilding
        fields = ['pap', 'name','construction_image', 'size', 'number_of_construction','rate', 'value_of_structures','created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new `Crop` instance, given the validated data.
        """
        return ConstructionBuilding.objects.create(**validated_data)


class CropSerializer(serializers.ModelSerializer):
    pap = serializers.SlugRelatedField(
        slug_field='first_name',
        queryset=ProjectAffectedPerson.objects.all()
    )
    
    class Meta:
        model = Crop
        fields = ['name', 'crop_image','description', 'quantity', 'quality', 'rate', 'rating', 
        'pap','value_of_crops','created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new `Crop` instance, given the validated data.
        """
        return Crop.objects.create(**validated_data)

class LandSerializer(serializers.ModelSerializer):
    pap = serializers.SlugRelatedField(
        slug_field='first_name',
        queryset=ProjectAffectedPerson.objects.all()
    )

    class Meta:
        model = Land
        fields = ['land_type', 'land_image','survey_no', 'pap','tenure', 'size', 'location', 'land_use', 
                    'land_services', 'rate','value_of_land', 'created', 'updated']

class TreeSerializer(serializers.ModelSerializer):
    pap = serializers.SlugRelatedField(
        slug_field='first_name',
        queryset=ProjectAffectedPerson.objects.all()
    )
    class Meta:
        model = Tree
        fields = ['pap', 'name', 'description','tree_image', 'quantity','rate', 'value_of_trees', 'created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new `Tree` instance, given the validated data.
        """
        pap= ProjectAffectedPerson.objects.filter(owner=self.request.user)
        Tree.objects.create(pap=pap)
    

class ProjectAffectedPersonSerializer(serializers.ModelSerializer):
    pap_crops = CropSerializer(many=True, read_only=True)
    pap_lands = LandSerializer(many=True, read_only=True)
    pap_construction= ConstructionBuildingSerializer(many=True, read_only=True)
    pap_trees= TreeSerializer(many=True, read_only=True)
    class Meta:
        model = ProjectAffectedPerson
        fields = ['first_name', 'last_name', 'pap_image','age', 'address', 
        'id_no','email','phone_number','pap_crops','total_value_of_crops','pap_lands','pap_trees',
        'pap_construction','created', 'updated']

    def create(self, validated_data):
        """
        Create and return a new `ProjectAffectedPerson` instance, given the validated data.
        """
        return ProjectAffectedPerson.objects.create(**validated_data)
    


    
