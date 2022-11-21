from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.api_root, name='main'),
    path('api/paps/', views.ProjectAffectedPersonList.as_view(), name='pap-list'),
    path('api/paps/<int:pk>/', views.ProjectAffectedPersonDetail.as_view(), name='pap-detail'),
    path('api/paps/<str:id_no>/', views.ProjectAffectedPersonName.as_view(), name='pap-name'),
    path('api/crops/', views.CropList.as_view(), name='crop-list'),
    path('api/crops/<int:pk>/', views.CropDetail.as_view(), name='crop-detail'),
    path('api/crops/<name>/', views.CropDetails.as_view(), name='crop-details'),
    path('api/crops/<first_name>/', views.PapCrop.as_view(), name='pap-crops'),
    path('api/building/', views.ConstructionBuildingList.as_view(), name='construction-list'),
    path('api/building/<int:pk>/', views.ConstructionBuildingDetail.as_view(), name='construction-detail'),
    path('api/building/<name>/', views.ConstructionDetails.as_view(), name='construction-details'),
    path('api/building/<first_name>/', views.PapConstructionView.as_view(), name='pap-construction'),
    path('api/trees/', views.TreeList.as_view(), name='tree-list'),
    path('api/trees/<int:pk>/', views.TreeDetail.as_view(), name='tree-detail'),
    path('api/trees/<name>/', views.TreeDetails.as_view(), name='tree-details'),
    path('api/trees/<first_name>/', views.PapTreeView.as_view(), name='pap-tree'),
    path('api/land/', views.LandList.as_view(), name='land-list'),
    path('api/land/<int:pk>/', views.LandDetail.as_view(), name='land-details'),
    path('api/land/<land_type>/', views.LandDetails.as_view(), name='land-details'),
    path('api/land/<first_name>/', views.PapLandView.as_view(), name='pap-land')
]
urlpatterns = format_suffix_patterns(urlpatterns)