from django.contrib import admin
from .models import Crop, Land, Tree, ProjectAffectedPerson, ConstructionBuilding, CropList


#Register your models here.
admin.site.register(CropList)
admin.site.register(Crop)
admin.site.register(Land)
admin.site.register(Tree)
admin.site.register(ProjectAffectedPerson)
admin.site.register(ConstructionBuilding)
