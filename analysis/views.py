from django.shortcuts import render
from api.models import *
from django.db.models import *
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers import *
from django.http import Http404
from rest_framework.reverse import reverse
from rest_framework import status, generics, renderers, filters
from rest_framework.decorators import api_view
from django.db.models.functions import *

# Create your views here.
#Analysis  root
@api_view(['GET'])
def Analysis_root(request, format = None):
   return Response({
      'number_of_crops': reverse('number-of-crops', request = request, format = format),
      'crops_rate_total': reverse('total-crops-rate', request = request, format = format),
      'minimum_crop_rate': reverse('minimum-crop-rate', request = request, format = format),
      'maximum_crop_rate': reverse('maximum-crop-rate', request = request, format = format),
      'average_crop_rate': reverse('average-crop-rate', request = request, format = format),
      'crops_rate_difference': reverse('crop-rate-difference', request = request, format = format),
      'maximum_crop_rating': reverse('crop-rating-maximum', request = request, format = format),
      'minimum_crop_rating': reverse('crop-rating-minimum', request = request, format = format),
      'average_crop_rating': reverse('crop-rating-average', request = request, format = format),
      'crop_rating_difference': reverse('crop-rating-difference', request = request, format = format),
      'number_of_land': reverse('number-of-land', request = request, format = format),
      'land_rate_total': reverse('total-land-rate', request = request, format = format),
      'minimum_land_rate': reverse('minimum-land-rate', request = request, format = format),
      'maximum_land_rate': reverse('maximum-land-rate', request = request, format = format),
      'average_land_rate': reverse('average-land-rate', request = request, format = format),
      'land_rate_difference': reverse('land-rate-difference', request = request, format = format),
      'number_of_construction': reverse('number-of-construction', request = request, format = format),
      'construction_rate_total': reverse('total-construction-rate', request = request, format = format),
      'minimum_construction_rate': reverse('minimum-construction-rate', request = request, format = format),
      'maximum_construction_rate': reverse('maximum-construction-rate', request = request, format = format),
      'average_construction_rate': reverse('average-construction-rate', request = request, format = format),
      'construction_rate_difference': reverse('construction-rate-difference', request = request, format = format),
      'number_of_trees': reverse('number-of-trees', request = request, format = format),
      'tree_rate_total': reverse('total-tree-rate', request = request, format = format),
      'minimum_tree_rate': reverse('minimum-tree-rate', request = request, format = format),
      'maximum_tree_rate': reverse('maximum-tree-rate', request = request, format = format),
      'average_tree_rate': reverse('average-tree-rate', request = request, format = format),
      'tree_rate_difference': reverse('tree-rate-difference', request = request, format = format)
   })


#Crops analysis
#Number of crops in the system
class CropAnalysisView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        number_of_crops = Crop.objects.all().aggregate(Count('name'))
        return Response(number_of_crops)

#Total value of crops
class TotalCropValueView(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Crop.objects.all().order_by('-created')
    serializer_class = CropSerializer


    def get(self, request, id):
            pap = ProjectAffectedPerson.objects.get(id=id)
            crop_rate = Crop.objects.all()
            crop_rate_value = crop_rate.rate = F('rate')
            crop_quantity = Crop.objects.all()
            crop_quantity_value = crop_quantity.quantity = F('quantity')
            crop_value_difference = crop_rate_value * crop_quantity_value
            owner = self.request.user
            total_value = Crop.objects.filter(owner=owner, pap=pap).aggregate(total_value_of_crops =Sum(crop_value_difference))
            return Response(total_value)

#Total value of trees
class TotalTreeValueView(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CropSerializer
    queryset = Tree.objects.all().order_by('-created')


    def get(self, request, id):
            pap = ProjectAffectedPerson.objects.get(id=id)
            tree_rate = Tree.objects.all()
            tree_rate_value = tree_rate.rate = F('rate')
            tree_quantity = Tree.objects.all()
            tree_quantity_value = tree_quantity.quantity = F('quantity')
            tree_value_difference = tree_rate_value * tree_quantity_value
            owner = self.request.user
            total_value = Tree.objects.filter(owner=owner, pap=pap).aggregate(total_value_of_trees =Sum(tree_value_difference))
            return Response(total_value)


#Total value of Construction
class TotalConstructionValueView(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ConstructionBuilding.objects.all().order_by('-created')
    serializer_class = ConstructionBuildingSerializer


    def get(self, request, id):
            pap = ProjectAffectedPerson.objects.get(id=id)
            construction_rate = ConstructionBuilding.objects.all()
            construction_rate_value = construction_rate.rate = F('rate')
            construction_size = ConstructionBuilding.objects.all()
            construction_size_value = construction_size.size = F('size')
            number_of_construction = ConstructionBuilding.objects.all()
            number_of_construction_value = number_of_construction.number_of_construction = F('number_of_construction')
            construction_value_difference = construction_rate_value * construction_size_value * number_of_construction_value
            owner = self.request.user
            total_value = ConstructionBuilding.objects.filter(owner=owner, pap=pap).aggregate(total_value_of_construction =Sum(construction_value_difference))
            return Response(total_value)

#Total value of Land
class TotalLandValueView(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LandSerializer
    queryset = Land.objects.all().order_by('-created')


    def get(self, request, id):
            pap = ProjectAffectedPerson.objects.get(id=id)
            land_rate = Land.objects.all()
            land_rate_value = land_rate.rate = F('rate')
            land_size = Land.objects.all()
            land_size_value = land_size.size = F('size')
            land_value_difference = land_rate_value * land_size_value
            user = self.request.user
            total_value = Land.objects.filter(user=user, pap=pap).aggregate(total_value_of_land =Sum(land_value_difference))
            return Response(total_value)

#Award View
class AwardView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LandSerializer, CropSerializer, TreeSerializer, ConstructionBuildingSerializer
    queryset = Crop.objects.all().order_by('-created')
    queryset = Tree.objects.all().order_by('-created')
    queryset = Land.objects.all().order_by('-created')
    queryset = ConstructionBuilding.objects.all().order_by('-created')
    
    def get(self, request, id):
        owner = self.request.user
        user = self.request.user
        pap = ProjectAffectedPerson.objects.get(id=id)
        #crops
        crop_rate = Crop.objects.all()
        crop_rate_value = crop_rate.rate = F('rate')
        crop_quantity = Crop.objects.all()
        crop_quantity_value = crop_quantity.quantity = F('quantity')
        crop_value_difference = crop_rate_value * crop_quantity_value
        total_value_crops = Crop.objects.filter(owner=owner, pap=pap).aggregate(total_value_of_crops =Sum(crop_value_difference))
        #trees
        tree_rate = Tree.objects.all()
        tree_rate_value = tree_rate.rate = F('rate')
        tree_quantity = Tree.objects.all()
        tree_quantity_value = tree_quantity.quantity = F('quantity')
        tree_value_difference = tree_rate_value * tree_quantity_value
        total_value_trees = Tree.objects.filter(owner=owner, pap=pap).aggregate(total_value_of_trees =Sum(tree_value_difference))
        #construction
        construction_rate = ConstructionBuilding.objects.all()
        construction_rate_value = construction_rate.rate = F('rate')
        construction_size = ConstructionBuilding.objects.all()
        construction_size_value = construction_size.size = F('size')
        number_of_construction = ConstructionBuilding.objects.all()
        number_of_construction_value = number_of_construction.number_of_construction = F('number_of_construction')
        construction_value_difference = construction_rate_value * construction_size_value * number_of_construction_value
        total_value_construction = ConstructionBuilding.objects.filter(owner=owner, pap=pap).aggregate(total_value_of_construction =Sum(construction_value_difference))
        #land
        land_rate = Land.objects.all()
        land_rate_value = land_rate.rate = F('rate')
        land_size = Land.objects.all()
        land_size_value = land_size.size = F('size')
        land_value_difference = land_rate_value * land_size_value
        total_value_land = Land.objects.filter(user=user, pap=pap).aggregate(total_value_of_land =Sum(land_value_difference))
        #Award
        def add(a, b, c, d):
            return a + b + c + d
            
        crops_value = total_value_crops.values()
        trees_value = total_value_trees.values()
        construction_value = total_value_construction.values()
        land_value = total_value_land.values()
        #award = sum(crops_value) + sum(trees_value) + sum(construction_value) + sum(land_value)
        award2 = add(a = sum(crops_value), b = sum(trees_value), c = sum(construction_value), d = sum(land_value))
        return Response(award2)

       

#Total rate of crops in the system
class CropRateSumView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        total_crops_rate = Crop.objects.all().aggregate(Sum('rate'))
        return Response(total_crops_rate)

#Minimum rate of crops in the system
class MinimumCropRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        minimum_crop_rate = Crop.objects.all().aggregate(Min('rate'))
        return Response(minimum_crop_rate)

#Maximum rate of crops in the system
class MaximumCropRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        minimum_crop_rate = Crop.objects.all().aggregate(Max('rate'))
        return Response(minimum_crop_rate)

#Average rate of crops in the system
class AverageCropRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        average_crop_price = Crop.objects.all().aggregate(Avg('rate'))
        return Response(average_crop_price)

#Rate difference of crops in the system
class CropRateDifferenceView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        rate_difference = Crop.objects.all().aggregate(Avg('rate'), Max('rate'), Min('rate'))
        return Response(rate_difference)



#Crops ratings
#Maximum rating in the system
class CropRatingHighView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        maximum_crop_ratings = Crop.objects.all().aggregate(Max('rating'))
        return Response(maximum_crop_ratings)

#Minimum rating in the system
class CropRatingLowView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        minimum_crop_ratings = Crop.objects.all().aggregate(Min('rating'))
        return Response(minimum_crop_ratings)

#Rating Average in the system
class CropRatingAverageView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        average_crop_ratings = Crop.objects.all().aggregate(Avg('rating'))
        return Response(average_crop_ratings)

#Rating Difference in the system
class CropRatingDifferenceView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        crop_rating_difference = Crop.objects.all().aggregate(Avg('rating'), Max('rating'), Min('rating'))
        return Response(crop_rating_difference)

#LAND
#Land analysis
#Number of Land in the system
class LandAnalysisView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        number_of_land = Land.objects.all().aggregate(Count('id'))
        return Response(number_of_land)

#Total rate of land in the system
class LandRateSumView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        total_land_rate = Land.objects.all().aggregate(Sum('rate'))
        return Response(total_land_rate)

#Minimum rate of land in the system
class MinimumLandRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        minimum_land_rate = Land.objects.all().aggregate(Min('rate'))
        return Response(minimum_land_rate)

#Maximum rate of land in the system
class MaximumLandRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        minimum_land_rate = Land.objects.all().aggregate(Max('rate'))
        return Response(minimum_land_rate)

#Average rate of land in the system
class AverageLandRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        average_land_rate = Land.objects.all().aggregate(Avg('rate'))
        return Response(average_land_rate)

#Rate difference of land in the system
class LandRateDifferenceView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        land_rate_difference = Land.objects.all().aggregate(Avg('rate'), Max('rate'), Min('rate'))
        return Response(land_rate_difference)


#Construction analysis
#Number of constructions in the system
class ConstructionAnalysisView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        number_of_construction = ConstructionBuilding.objects.all().aggregate(Count('id'))
        return Response(number_of_construction)

#Total rate of constructions in the system
class ConstructionRateSumView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        total_construction_rate = ConstructionBuilding.objects.all().aggregate(Sum('rate'))
        return Response(total_construction_rate)

#Minimum rate of construction in the system
class MinimumConstructionRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        minimum_construction_rate = ConstructionBuilding.objects.all().aggregate(Min('rate'))
        return Response(minimum_construction_rate)

#Maximum rate of crops in the system
class MaximumConstructionRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        minimum_construction_rate = ConstructionBuilding.objects.all().aggregate(Max('rate'))
        return Response(minimum_construction_rate)

#Average rate of construction in the system
class AverageConstructionRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        average_construction_rate = ConstructionBuilding.objects.all().aggregate(Avg('rate'))
        return Response(average_construction_rate)

#Rate difference of construction in the system
class ConstructionRateDifferenceView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        construction_rate_difference = ConstructionBuilding.objects.all().aggregate(Avg('rate'), Max('rate'), Min('rate'))
        return Response(construction_rate_difference)


#Tree analysis
#Number of trees in the system
class TreeAnalysisView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        number_of_trees = Tree.objects.all().aggregate(Count('id'))
        return Response(number_of_trees)

#Total rate of trees in the system
class TreeRateSumView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        total_tree_rate = Tree.objects.all().aggregate(Sum('rate'))
        return Response(total_tree_rate)

#Minimum rate of trees in the system
class MinimumTreeRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        minimum_tree_rate = Tree.objects.all().aggregate(Min('rate'))
        return Response(minimum_tree_rate)

#Maximum price of trees in the system
class MaximumTreeRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        minimum_tree_rate = Tree.objects.all().aggregate(Max('rate'))
        return Response(minimum_tree_rate)

#Average price of trees in the system
class AverageTreeRateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        average_tree_rate = Tree.objects.all().aggregate(Avg('rate'))
        return Response(average_tree_rate)

#Rate difference of trees in the system
class TreeRateDifferenceView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        tree_rate_difference = Tree.objects.all().aggregate(Avg('rate'), Max('rate'), Min('rate'))
        return Response(tree_rate_difference)

