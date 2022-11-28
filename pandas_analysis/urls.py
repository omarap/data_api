from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pandas_analysis import views

urlpatterns = (
    path('', views.pandas_analysis_root, name='pandas-analysis'),
    path("papdata/", views.ProjectAffectedPersionJSONView.as_view(), name='pap-data'),
    path("papdata/download/", views.ProjectAffectedPersionPandasView.as_view(), name='pap-data-download'),
    path("construction-data/download/", views.ConstructionPandasView.as_view(), name='construction-data-download'),
    path("trees-data/download/", views.TreePandasView.as_view(), name='trees-data-download'),
    path("crops-data/download/", views.CropPandasView.as_view(), name='crops-data-download'),
    path("land-data/download/", views.LandPandasView.as_view(), name='land-data-download')               
)

# The following is required to support extension-style formats (e.g. /data.csv)
urlpatterns = format_suffix_patterns(urlpatterns)