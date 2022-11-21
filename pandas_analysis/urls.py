from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pandas_analysis import views

urlpatterns = (
    path('', views.pandas_analysis_root, name='pandas-analysis'),
     path("papdata/", views.ProjectAffectedPersionJSONView.as_view(), name='pap-data'),
    path("papdata/download/", views.ProjectAffectedPersionPandasView.as_view(), name='pap-data-download')    
)

# The following is required to support extension-style formats (e.g. /data.csv)
urlpatterns = format_suffix_patterns(urlpatterns)