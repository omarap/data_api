from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pandas_analysis import views

urlpatterns = (
    path('', views.pandas_analysis_root, name='pandas-analysis'),
    path("papdata/", views.ProjectAffectedPersionJSONView.as_view(), name='pap-data'),
    path("papdata/download/", views.ProjectAffectedPersionPandasView.as_view(), name='pap-data-download'),
    path("", views.PAPListPDF.as_view({'get':'list'}), name='pap-list-pdf'),
    path("listpaps/", views.ListPAPs.as_view({'get': 'list'}), name='list-paps'),
    path("pap_detail_pdf/", views.PAPListPDF.as_view({'get':'retrieve'}), name='pap-details-pdf'),
    path("constructiondata/download/", views.ConstructionPandasView.as_view(), name='construction-data-download'),
    path("treesdata/download/", views.TreePandasView.as_view(), name='trees-data-download'),
    path("cropsdata/download/", views.CropPandasView.as_view(), name='crops-data-download'),
    path("landdata/download/", views.LandPandasView.as_view(), name='land-data-download')               
)

# The following is required to support extension-style formats (e.g. /data.csv)
urlpatterns = format_suffix_patterns(urlpatterns)