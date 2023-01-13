from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.api_root, name='main'),
    path('api/paps/', views.ProjectAffectedPersonList.as_view(), name='pap-list'),
    path('api/paps/<int:pk>/', views.ProjectAffectedPersonDetail.as_view(), name='pap-detail'),
    path('api/paps/<first_name>/', views.ProjectAffectedPersonNameView.as_view({'get': 'list'}), name='pap-name'),
    path('api/crops/', views.CropList.as_view(), name='crop-list'),
    path('api/croplist/', views.CropListName.as_view(), name='crop-list-names'),
    path('api/croplist/<int:pk>/', views.CropListDetailName.as_view(), name='crop-list-detail'),
    path('api/crops/<int:pk>/', views.CropDetail.as_view(), name='crop-detail'),
    path('api/crops/<name>/', views.CropDetailNameView.as_view({'get': 'list'}), name='crop-detail-name'),
    path('api/crops/<name>/count/', views.CropDetailNameView.as_view({'get': 'count_crops'}), name='crop-detail-name'),
    path('api/papcrops/<first_name>/', views.PapCrop.as_view({'get': 'list'}), name='pap-crops'),
    path('api/building/', views.ConstructionBuildingList.as_view(), name='construction-list'),
    path('api/building/<int:pk>/', views.ConstructionBuildingDetail.as_view(), name='construction-detail'),
    path('api/building/<name>/', views.ConstructionDetailNameView.as_view({'get': 'list'}), name='construction-detail-name'),
    path('api/building/<name>/count/', views.ConstructionDetailNameView.as_view({'get': 'count_construction'}), name='construction-detail-name'),
    path('api/papbuilding/<first_name>/', views.PapConstructionView.as_view({'get': 'list'}), name='pap-construction'),
    path('api/trees/', views.TreeList.as_view(), name='tree-list'),
    path('api/trees/<int:pk>/', views.TreeDetail.as_view(), name='tree-detail'),
    path('api/trees/<name>/', views.TreeDetailNameView.as_view({'get': 'list'}), name='tree-detail-name'),
    path('api/trees/<name>/count/', views.TreeDetailNameView.as_view({'get': 'count_tree'}), name='tree-detail-name-count'),
    path('api/treepap/<first_name>/', views.PapTreeView.as_view({'get': 'list'}), name='pap-tree'),
    path('api/land/', views.LandList.as_view(), name='land-list'),
    path('api/land/<int:pk>/', views.LandDetail.as_view(), name='land-details'),
    path('api/land/<land_type>/', views.LandDetailNameView.as_view({'get': 'list'}), name='land-detail-name'),
    path('api/land/<land_type>/count/', views.LandDetailNameView.as_view({'get': 'count_land'}), name='land-detail-name'),
    path('api/papland/<first_name>/', views.PapLandView.as_view({'get': 'list'}), name='pap-land'),
    path('api/upload/papcsv/', views.UploadFileView.as_view(), name='upload-file-csv'),
    path('api/upload/cropcsv/', views.UploadCropFileView.as_view(), name='upload-crop-file-csv')
]
urlpatterns = format_suffix_patterns(urlpatterns)