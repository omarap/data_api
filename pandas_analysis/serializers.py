from rest_framework import serializers
from api.models import *

class ProjectAffectedPersionPandasSerializer(serializers.ModelSerializer):
    pap_crops = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='crop-detail'
    )

    pap_lands = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='land-details'
    )
    pap_trees = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='tree-detail'
    )
    pap_construction = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='construction-detail'
    )
    
    class Meta:
        model = ProjectAffectedPerson
        fields = ['pap_image', 'first_name', 'last_name', 'age', 'address', 'id_no','email', 
        'phone_number','trees', 'crops','land','construction','pap_crops','pap_lands','pap_trees',
        'pap_construction','created', 'updated']

    